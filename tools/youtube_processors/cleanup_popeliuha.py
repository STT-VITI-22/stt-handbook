import os
import shutil

base_dir = 'dataset/youtube/popeliuha'

# 1. Delete entirely irrelevant directories
for d in ['CSharp_Automation', 'Git', 'MySQL']:
    path = os.path.join(base_dir, d)
    if os.path.exists(path):
        shutil.rmtree(path)

# 2. Keep only specific files in Tools_and_API
tools_dir = os.path.join(base_dir, 'Tools_and_API')
tools_keep = ['45-_Що_таке_API_і_як_воно_працює.md']
if os.path.exists(tools_dir):
    for f in os.listdir(tools_dir):
        if f not in tools_keep:
            os.remove(os.path.join(tools_dir, f))

# 3. Keep only specific files in Career_and_Interviews
career_dir = os.path.join(base_dir, 'Career_and_Interviews')
career_keep = [
    'Відповіді_на_Співбесіду_Тестувальника-_Види-Типи_тестування.md',
    'Відповіді_на_Співбесіду_Тестувальника-_Тестова_документація.md',
    '95-_Топ_20_питань_на_співбесіду_на_Тестувальника_в_Україні.md',
    'Роман_Марінський-_Внутрішня_тестова_співбесіда_-_Загальні_питання.md'
]
if os.path.exists(career_dir):
    for f in os.listdir(career_dir):
        if f not in career_keep:
            os.remove(os.path.join(career_dir, f))

# 4. Clean QA_Fundamentals (remove C# leftovers, vlogs, tools)
qa_dir = os.path.join(base_dir, 'QA_Fundamentals')
qa_keep = [
    '13-_Що_таке_Test_Scenario_і_Test_Сondition.md',
    '27-_Additional_types_of_testing-_Testing_pyramid.md',
    '29-_Всі_типи_тестування_100Plus.md',
    '34-_Як_будувати_Таблиці_істинності_для_ТПР.md', # Will move this
    '40-_Дослідницьке_тестування-_Вгадування_помилок-_Тестування_чек-лістів.md',
    '42-_Frontend_та_Backend_простими_словами.md',
    '43-_Client-server_architecture-_HTTP-_HTTPS.md',
    '61-_Frontend_тестування-_Веб-елементи_та_дії_над_ними.md',
    '80-_Логи_в_тестуванні.md',
    '81-_Метрики_в_тестуванні.md',
    '82-_Оцінювання_задач.md',
    '83-_Ризики_в_тестуванні.md',
    '84-_Що_таке_Definition_of_Ready_та_Definition_of_Done.md',
    '86-_Traceability_Matrix_and_Impact_analysis_in_Ukrainian.md',
    '88-_Master_test_plan-_Level_test_plan_and_other_scary_documents.md',
    '8-_Створення_Чек-ліста_на_практиці.md',
    'Конспект_з_Тестування_ПЗ_Українською.md',
    'ПРАКТИЧНИЙ_КУРС_МАНУАЛЬНОГО_ТЕСТУВАННЯ.md',
    'CI_CD_для_тестувальників-_Середовища-_Environments_87_менюал_-_42_авто.md',
    'Як_протестувати_Backend.md'
]
if os.path.exists(qa_dir):
    for f in os.listdir(qa_dir):
        if f not in qa_keep:
            os.remove(os.path.join(qa_dir, f))
            
    # Move Table of Truth to Test Design
    tt_src = os.path.join(qa_dir, '34-_Як_будувати_Таблиці_істинності_для_ТПР.md')
    if os.path.exists(tt_src):
        shutil.move(tt_src, os.path.join(base_dir, 'Test_Design_Techniques', '34-_Як_будувати_Таблиці_істинності_для_ТПР.md'))

print("Очищення завершено. Видалено всі офтопні відео, залишено лише теорію ТТПЗ.")
