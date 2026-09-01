import os, glob, re

for filepath in glob.glob('dataset/articles/ibm/*.md'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove newsletter subscriptions
    content = re.sub(r'## The latest tech news.*?(?=\n## |\n\n)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'Stay up to date on the most important.*?Privacy Statement.*?\)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'## Thank you! You are subscribed.', '', content, flags=re.IGNORECASE)
    content = re.sub(r'Discover expertly curated insights.*?\[Subscribe today\].*?\)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove observability video block
    content = re.sub(r'### 6 observability myths.*?decision-making.', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove any random "Explore DevOps" hanging lines
    content = re.sub(r'\[Explore DevOps\].*?\)', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\[Explore Confluent\].*?\)', '', content, flags=re.IGNORECASE)
    
    # Clean up excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    with open(filepath, 'w') as f:
        f.write(content)

