# EXCEL TEMPLATES INTEGRATION GUIDE
## TestCase-Checklist-Bug-Template.xlsx Аналіз та Інтеграція

**Дата аналізу:** 18 серпня 2026 року
**Файл:** `dataset/practical_tasks/TestCase-Checklist-Bug-Template.xlsx`
**Статус:** ✅ Готовий до інтеграції та розширення

---

## 1. ПОТОЧНА СТРУКТУРА ФАЙЛУ

### 📊 Огляд листів (6 листів):

| № | Назва листа | Тип | Статус | Опис |
|---|------------|------|--------|------|
| 1 | Business Requirement | Reference | ✅ | Приклад бізнес-вимог для тестування |
| 2 | **Test Case Template** | Template | ✅ | **Основний шаблон для test cases** |
| 3 | **Checklist Template** | Template | ✅ | **Шаблон для тестової чек-листи** |
| 4 | Bug 1 | Example | ✅ | Приклад баг-репорту #1 |
| 5 | Bug 2 | Example | ✅ | Приклад баг-репорту #2 |
| 6 | **Bug Template** | Template | ✅ | **Основний шаблон для bug reports** |

### 📋 Test Case Template (Лист 2)

**Колонки:**
```
A - Number              (ID тест-кейсу)
B - Test Name           (Назва тесту)
C - Description         (Опис кроків/дій)
D - PreCondition        (Передумови)
E - Test Data           (Тестові дані)
F - Priority            (Пріоритет: High/Medium/Low)
G - Expected Result     (Очікуваний результат)
H - Tester              (ПІБ тестувальника)
I - Status              (Статус: Passed/Failed/Not Tested/Skipped)
J - Comment             (Коментарі)
K-L - Додаткові Priority/Status
```

**Приклад заповненого рядка:**
```
1 | User Accounts | User with two bank accounts can observe both accounts |
  | User should have two active accounts | High |
  | User will see two accounts in list | Ozan | Passed | [comment]
```

### 📋 Checklist Template (Лист 3)

**Колонки:**
```
A - Number              (ID пункту чек-листи)
B - Checklist Description (Опис що перевіряти)
C - Status              (Статус: Passed/Failed/Not Tested)
D - Status              (Альтернативна колонка статусу)
```

**Статус значення:**
- ✅ Passed
- ❌ Failed
- ⚪ Not Tested

### 📋 Bug Template (Лист 6)

**Колонки:**
```
A - Bug Title           (Назва проблеми)
B - Bug Priority        (Пріоритет: Critical/High/Medium/Low/Trivial)
C - Description         (Детальний опис)
D - Attachments         (Посилання на скрін-шоти)
E - Priority            (Додаткова пріоритет колонка)
```

**Формат опису:**
```
Summary:
Steps to Reproduce:
1. [крок 1]
2. [крок 2]
3. [крок 3]

Expected Results:
[очікуваний результат]

Actual Results:
[фактичний результат]
```

---

## 2. РЕКОМЕНДАЦІЇ ДО РОЗШИРЕННЯ ФАЙЛУ

### 2.1 Best Practices для Test Cases
```
Рекомендації по заповненню Test Cases:
- Що писати у Description
- Як формулювати Expected Results
- Шаблони для різних типів тестів (Positive, Negative, Edge cases)
```

### 2.2 Bug Report Guidelines
```
Як писати баг-репорти:
- Формулювання Bug Title
- Класифікація Priority
- Детальні кроки відтворення (Steps to Reproduce)
- Розрізнення Expected vs Actual Results
```

### 2.3 Status & Priority Reference
```
Довідник значень:
- Статуси: Passed, Failed, Blocked, Not Tested, Skipped
- Пріоритети Test Cases: Critical, High, Medium, Low, Trivial
- Пріоритети Bugs: Critical, High, Medium, Low, Trivial
```

---

## 3. ДОКУМЕНТАЦІЯ ДЛЯ STUDENT USAGE

### 3.1 Для stt-manual-testing (Ch 3.6)

**TEMPLATE_GUIDE.md структура:**
```markdown
# Test Case Template Guide

## Як використовувати шаблон

### Колонка: Number
- ID тест-кейсу (1, 2, 3...)
- Унікальний у межах документа
- Для відстеження та посилання

### Колонка: Test Name
- Коротке ім'я тесту (2-5 слів)
- Приклад: "User Login with Valid Credentials"

### Колонка: Description (Action/Steps)
- Детальні кроки виконання тесту
- Нумерованого списку (1., 2., 3.)
- Кожен крок - окремо дію

### Колонка: PreCondition
- Що повинно бути готово перед тестом
- Приклад: "User має бути зареєстрований"

### Колонка: Test Data
- Конкретні значення для тесту
- Приклад: "Username: testuser@example.com, Password: Test123"

### Колонка: Priority
- Важливість тесту
- Values: High (ОБОВ'ЯЗКОВИЙ), Medium (ВАЖЛИВИЙ), Low (КОРИСНИЙ)

### Колонка: Expected Result
- Що повинно статися після кроків
- Має бути перевірити чітко
- Приклад: "Користувач отримує 'Login Successful' повідомлення"

### Колонка: Tester
- ПІБ людини, яка виконує тест
- Для відповідальності та відстеження

### Колонка: Status
- Результат виконання тесту
- ✅ Passed - тест пройшов успішно
- ❌ Failed - тест провалився
- ⚪ Not Tested - ще не виконувався
- 🔄 Skipped - пропущений з причини

## Приклади TEST CASES

### Приклад 1: Позитивний тест (Positive Test)
```
Number: 1
Test Name: Successful User Login
Description:
  1. Відкрити сторінку логіну
  2. Ввести коректне ім'я користувача
  3. Ввести коректний пароль
  4. Натиснути кнопку "Login"
PreCondition: User account має існувати
Test Data: Username=john@test.com, Password=Pass123
Priority: High
Expected Result: Користувач перенаправляється на Home Page
Status: Passed
```

### Приклад 2: Негативний тест (Negative Test)
```
Number: 2
Test Name: Login with Invalid Password
Description:
  1. Відкрити сторінку логіну
  2. Ввести коректне ім'я користувача
  3. Ввести НЕПРАВИЛЬНИЙ пароль
  4. Натиснути кнопку "Login"
PreCondition: User account має існувати
Test Data: Username=john@test.com, Password=WrongPass
Priority: High
Expected Result: Система показує помилку "Invalid credentials"
Status: Failed (Bug #123: Error message not displayed)
```

### Приклад 3: Edge Case тест
```
Number: 3
Test Name: Login with Empty Username
Description:
  1. Відкрити сторінку логіну
  2. НЕ вводити ім'я користувача (залишити порожньо)
  3. Ввести пароль
  4. Натиснути "Login"
PreCondition: Page loaded successfully
Test Data: Username=[empty], Password=Pass123
Priority: Medium
Expected Result: Система показує помилку "Username is required"
Status: Not Tested
```

## Best Practices

1. **Повторюваність**: Тест повинен мати однаковий результат при повторенні
2. **Незалежність**: Кожен тест повинен працювати окремо, без залежності від інших
3. **Розуміння**: Будь-який QA повинен зрозуміти тест за описом
4. **Однозначність**: Очікуваний результат має бути чітко перевірити
```
```

### 3.2 Для stt-bug-reporting (Ch 8.7)

**TEMPLATE_GUIDE.md структура:**
```markdown
# Bug Report Template Guide

## Як писати баг-репорти

### Колонка: Bug Title
- Коротко описати проблему (5-10 слів)
- Мати на увазі Summary
- Приклад: "Login button not working on mobile"

### Колонка: Bug Priority
- Як критична проблема для користувача
- Critical: Система не працює взагалі
- High: Основна функція не працює
- Medium: Функція працює з дефектами
- Low: Невелика проблема, але заважає
- Trivial: Косметичні проблеми (опечатка, alignment)

### Колонка: Description
- **Summary**: Коротке описання дефекту
- **Steps to Reproduce**: Номерований список дій для відтворення
- **Expected Results**: Що повинно статися
- **Actual Results**: Що насправді станеться

### Колонка: Attachments
- Посилання на скріншоти
- Посилання на відео
- Лог-файли при необхідності

## Приклади BUG REPORTS

### Bug Report Приклад 1: Critical

```
Bug Title: "Database Connection Lost After Login"

Bug Priority: CRITICAL

Description:
Summary:
  User loses access to application after successful login.
  Database queries timeout and user sees error page.

Steps to Reproduce:
  1. Log in to the application with valid credentials
  2. Wait for page to load completely
  3. Click on "View Profile" button
  4. Observe the response time

Expected Results:
  Profile page loads within 2 seconds
  User profile information is displayed correctly
  No error messages appear

Actual Results:
  Page loads slowly (15+ seconds)
  "Database Connection Error" message appears
  User is redirected back to login page
  Database logs show connection pool exhaustion

Attachments:
  Screenshot_error_page.png
  error_logs_20260818.txt
  database_metrics_graph.png
```

### Bug Report Приклад 2: Medium

```
Bug Title: "Validation Error Message Appears Twice"

Bug Priority: MEDIUM

Description:
Summary:
  When user submits form with invalid email,
  validation error appears twice on the page.

Steps to Reproduce:
  1. Go to Registration page
  2. Fill all fields except email
  3. Enter invalid email (e.g., "user@")
  4. Click "Register" button
  5. Observe the error messages

Expected Results:
  Single error message appears: "Please enter valid email"
  User can correct the email and resubmit

Actual Results:
  TWO identical error messages appear
  Only first message can be dismissed
  Second message remains visible
  User cannot proceed with form submission

Attachments:
  duplicate_error_screenshot.png
```

### Bug Report Приклад 3: Low (UI/UX)

```
Bug Title: "Button Text Misaligned in Safari Browser"

Bug Priority: LOW

Description:
Summary:
  "Login" button text appears misaligned in Safari browser.
  Text is centered in Chrome, but left-aligned in Safari.

Steps to Reproduce:
  1. Open website in Safari browser (macOS)
  2. Navigate to login page
  3. Observe the "Login" button alignment
  4. Compare with Chrome browser

Expected Results:
  Button text is centered in all browsers

Actual Results:
  Button text is left-aligned in Safari
  Looks unprofessional
  Same page renders correctly in Chrome/Firefox

Attachments:
  safari_button_issue.png
  chrome_button_correct.png
```

## Best Practices для Bug Reports

1. **Reproducible**: Bug має бути відтворити повторно
2. **Specific**: Не писати "Something doesn't work"
3. **Evidence**: Скріншоти/відео значно прискорюють розуміння
4. **Measurable**: "Slow response" → "Takes 15+ seconds to load"
5. **Isolated**: Описати одну проблему на баг-репорт
6. **Complete**: Надати всю інформацію для розслідування

## Priority vs Severity

- **Priority** = Як швидко це потрібно виправити (Critical/High/Medium/Low)
- **Severity** = Наскільки сильно це впливає на функціональність
```

---

## 4. ПЛАН РОЗШИРЕННЯ ФАЙЛУ

### 4.1 Негайні дії (Week 1-2)

- [ ] Копіювати Лист 2 → TEST_CASE_TEMPLATE.xlsx
- [ ] Копіювати Лист 6 → BUG_REPORT_TEMPLATE.xlsx
- [ ] Додати 3-4 нові приклади Test Cases до файлу
- [ ] Додати 3 нові приклади Bug Reports до файлу
- [ ] Створити TEMPLATE_GUIDE.md для обох

### 4.2 Розширення контенту (Week 2-3)

- [ ] **Новий лист: "Test Case Scenarios"**
  - Positive Test Cases (Happy Path)
  - Negative Test Cases (Error Handling)
  - Edge Case Tests (Boundary Values)
  - Integration Tests (Multiple Features)

- [ ] **Новий лист: "Bug Report Classifications"**
  - Functional Bugs
  - Performance Bugs
  - UI/UX Bugs
  - Security Bugs
  - Compatibility Bugs

- [ ] **Новий лист: "Real-World Examples"**
  - 5 реальних test cases з банківської системи
  - 5 реальних bug reports з веб-додатка

### 4.3 Advanced Features (Week 3-4)

- [ ] Додати data validation (dropdown lists)
- [ ] Додати цвітні формати для Priority/Status
- [ ] Додати conditional formatting (Red for Failed, Green for Passed)
- [ ] Додати pivot tables для аналізу результатів
- [ ] Додати chart для відслідження прогресу

---

## 5. ЗБЕРЕЖЕННЯ ФАЙЛІВ

### Рекомендована структура папок:

```
dataset/practical_tasks/
├── TestCase-Checklist-Bug-Template.xlsx (MASTER FILE - зберігати нетронутим)
│
├── stt-manual-testing/
│   ├── templates/
│   │   ├── TEST_CASE_TEMPLATE_BLANK.xlsx
│   │   ├── TEST_CASE_TEMPLATE_FILLED.xlsx
│   │   └── GUIDE.md
│   └── examples/
│       ├── Banking_System_TestCases.xlsx
│       ├── E-Commerce_TestCases.xlsx
│       └── Social_Media_TestCases.xlsx
│
├── stt-bug-reporting/
│   ├── templates/
│   │   ├── BUG_REPORT_TEMPLATE_BLANK.xlsx
│   │   ├── BUG_REPORT_TEMPLATE_FILLED.xlsx
│   │   └── GUIDE.md
│   └── examples/
│       ├── Critical_Bugs_Examples.xlsx
│       ├── Medium_Bugs_Examples.xlsx
│       └── Low_Bugs_Examples.xlsx
│
└── stt-pz-3-jest-api/ (for API testing examples)
    ├── mock-data/
    │   ├── test_case_mocks.json
    │   └── bug_report_mocks.json
    └── examples/
        ├── API_Test_Cases.xlsx
        └── API_Bug_Reports.xlsx
```

---

## 6. ІНТЕГРАЦІЯ З HANDBOOK

### Оновлення PRACTICAL_TASKS_INTEGRATION.md

Додати новий розділ:

```markdown
### 4.3 Excel Templates & Resources

**Основні шаблони:**
- TEST_CASE_TEMPLATE.xlsx — шаблон для création test cases
- BUG_REPORT_TEMPLATE.xlsx — шаблон для bug reporting
- CHECKLIST_TEMPLATE.xlsx — шаблон для тестової чек-листи

**Розташування:** `dataset/practical_tasks/`

**Як використовувати:**
1. Скопіюйте BLANK версію шаблону
2. Заповніть дані за гайдом TEMPLATE_GUIDE.md
3. Порівняйте з FILLED версією для прикладу
4. Сабмітьте заповнений файл як част проекту
```

### Оновлення HANDBOOK_STRUCTURE.md

Добавити у розділи Ch 3.6 (stt-manual-testing):

```
**Ресурси:**
- TEST_CASE_TEMPLATE.xlsx (blank)
- TEST_CASE_EXAMPLES.xlsx (з реальними прикладами)
- TEMPLATE_GUIDE.md (повна документація)
```

---

## 7. ТЕХНІЧНІ ДЕТАЛИ

### Шаблон можна редагувати:
- ✅ В Excel / Google Sheets
- ✅ В libre Office
- ✅ На Excel Online
- ✅ Експортувати в CSV для аналізу

### Порядок рекомендованих дій:

1. **Stage 1**: Розташувати файли у правильних папках
2. **Stage 2**: Створити TEMPLATE_GUIDE.md для кожного шаблону
3. **Stage 3**: Додати приклади заповнених файлів
4. **Stage 4**: Оновити документацію посібника (PRACTICAL_TASKS_INTEGRATION.md)
5. **Stage 5**: Commit до git з описанням змін

---

## 8. СТАТУС

✅ Аналіз структури завершено
✅ Рекомендації підготовлені
⏳ Очікування на реалізацію

**Наступні кроки:** Копіювання файлів, розширення контенту та інтеграція з документацією.

---

**Створено:** 18 серпня 2026
**Автор:** Claude Code Analysis
**Версія:** 1.0
