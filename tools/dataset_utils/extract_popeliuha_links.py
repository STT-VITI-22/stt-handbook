import zipfile
import xml.etree.ElementTree as ET
import re
import os
import json
import urllib.request

xlsx_path = 'popeliuha.xlsx'
out_dir = 'dataset/pptx_doc/popeliuha/raw'
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(xlsx_path, 'r') as z:
    # 1. Parse sharedStrings
    shared_strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        root = ET.fromstring(z.read('xl/sharedStrings.xml'))
        ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        for si in root.findall('main:si', ns):
            t = si.find('main:t', ns)
            if t is not None:
                shared_strings.append(t.text or "")
            else:
                # sometimes text is inside <r><t>
                texts = [rt.text for rt in si.findall('.//main:t', ns) if rt.text]
                shared_strings.append("".join(texts))
                
    # 2. Parse rels for URLs
    rels_map = {}
    rels_root = ET.fromstring(z.read('xl/worksheets/_rels/sheet1.xml.rels'))
    ns_rels = {'rels': 'http://schemas.openxmlformats.org/package/2006/relationships'}
    for rel in rels_root.findall('rels:Relationship', ns_rels):
        rels_map[rel.attrib['Id']] = rel.attrib.get('Target')

    # 3. Parse sheet1
    sheet_root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    ns_main = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    
    # map row to url
    row_url = {}
    hyperlinks = sheet_root.find('main:hyperlinks', ns_main)
    if hyperlinks is not None:
        for hl in hyperlinks.findall('main:hyperlink', ns_main):
            ref = hl.attrib.get('ref') # e.g. C3
            rid = hl.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            if ref and rid:
                match = re.match(r'[A-Z]+(\d+)', ref)
                if match:
                    row = int(match.group(1))
                    if rid in rels_map:
                        row_url[row] = rels_map[rid]
                        
    # map row to title
    row_title = {}
    sheetData = sheet_root.find('main:sheetData', ns_main)
    for row_elem in sheetData.findall('main:row', ns_main):
        row_idx = int(row_elem.attrib['r'])
        for c in row_elem.findall('main:c', ns_main):
            ref = c.attrib.get('r')
            if ref and ref.startswith('B'):
                # Extract number to be safe
                col_match = re.match(r'B(\d+)', ref)
                if col_match and int(col_match.group(1)) == row_idx:
                    t = c.attrib.get('t')
                    v = c.find('main:v', ns_main)
                    if v is not None:
                        val = v.text
                        if t == 's':
                            val = shared_strings[int(val)]
                        row_title[row_idx] = val.strip()

presentations = []
for row, url in row_url.items():
    title = row_title.get(row, f"presentation_row_{row}")
    # Replace invalid chars for filename
    clean_title = re.sub(r'[<>:"/\\|?*]', '_', title)
    presentations.append({
        'row': row,
        'title': clean_title,
        'url': url
    })

# Save meta
with open(os.path.join(out_dir, 'meta.json'), 'w', encoding='utf-8') as f:
    json.dump(presentations, f, ensure_ascii=False, indent=2)

print(f"Found {len(presentations)} presentations.")

# Download each
for p in presentations:
    url = p['url']
    if 'docs.google.com/presentation' in url:
        # Convert /edit or /view to /export/pdf
        export_url = re.sub(r'/edit.*$', '/export/pdf', url)
        export_url = re.sub(r'/view.*$', '/export/pdf', export_url)
    else:
        export_url = url
        
    filename = f"{p['row']:02d}_{p['title']}.pdf"
    filepath = os.path.join(out_dir, filename)
    print(f"Downloading {filename} from {export_url}...")
    try:
        urllib.request.urlretrieve(export_url, filepath)
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

