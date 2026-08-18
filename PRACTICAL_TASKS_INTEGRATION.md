# ПРАКТИЧНІ ЗАВДАННЯ — Інтеграція у HANDBOOK структуру

**Документ:** Рекомендації з інтеграції практичних уроків (stt-manual-testing, stt-pz-1 до stt-pz-5, stt-bug-reporting) у посібник та dataset

**Дата:** 18 серпня 2026 року
**Оновлено:** 18 серпня 2026 року (додано stt-manual-testing та stt-bug-reporting)

---

## 1. ОБЗОР ПРАКТИЧНИХ ЗАВДАНЬ (ВСЬОГО 8 ПРОЕКТІВ)

### Таблиця відповідності практичних завдань до розділів посібника

| № | Назва | Технологія | Фокус | Розділ(и) посібника | Тип тесту |
|---|-------|-----------|-------|-----------------|----------|
| **stt-manual-testing** 🆕 | Manual Testing & Test Case Design | Manual (Spreadsheet/JIRA) | Test Case створення, Manual execution | Ch 3 (Процеси тестування) | Manual |
| **stt-pz-1** | Unit Testing Basics | Mocha + Chai | Unit тестування, BDD/TDD основи | Ch 7 (Техніки дизайну) | Unit |
| **stt-pz-2** | TDD Methodology | Jest | Test-Driven Development | Ch 9 (Agile/DevOps), Ch 13 (Автоматизація) | Unit |
| **stt-pz-3** | API Testing & Mocking | Jest | API тестування, Mock дані | Ch 11 (Технічні основи) | API |
| **stt-pz-4** | BDD with Jest | Jest | Behavior-Driven Development | Ch 9 (Agile/DevOps), Ch 13 (Автоматизація) | Unit/BDD |
| **stt-pz-5** | E2E Testing | Cypress | End-to-End тестування | Ch 5 (Рівні тестування), Ch 13 (Автоматизація) | E2E |
| **stt-bug-reporting** 🆕 | Bug Reporting & Defect Management | JIRA/Bugzilla | Bug Report, RCA, Defect Lifecycle | Ch 8 (Управління дефектами) | Manual |
| **stt-elk-mcp-logging** 🆕🆕 | ELK + MCP AI Log Analysis | ELK + MCP + Claude | Logging, Monitoring, AI Analysis | Ch 12 (Метрики & Quality) | Integration/Monitoring |

---

## 2. ДЕТАЛІЗОВАНА ІНТЕГРАЦІЯ В HANDBOOK_STRUCTURE.md

### 2.0 CHAPTER 3: ПРОЦЕСИ ТА ЦИКЛИ ТЕСТУВАННЯ

**Добавити новий підрозділ:**

```
| 3.6 Практичне завдання: Manual Testing та Test Case Design |
- Практичний проект stt-manual-testing
- Створення тестових сценаріїв для реальних додатків
- Структура Test Case (ID, Title, Prerequisites, Steps, Expected Results)
- Позитивне та негативне тестування
- Тест-дизайн техніки у практиці
- Test Execution та документування результатів
- Ресурс: https://github.com/STT-VITI-22/stt-manual-testing
| RWP ✓ / DATASET(stt-manual-testing, QALight: osnovi) / MODERN ✓ |
```

**Важливість:** Цей розділ на початку посібника познайомлює з основами manual testing перед переходом до автоматизації.

---

### 2.1 CHAPTER 7: ТЕХНІКИ ТЕСТУВАННЯ ТА ДИЗАЙН

**Добавити новий підрозділ:**

```
| 7.8 Практичне завдання: Unit тестування з Mocha/Chai |
- Практичний проект stt-pz-1
- Налаштування браузерного тестового середовища
- BDD/TDD підходи в Mocha
- Assertion бібліотека Chai
- Browser-based test execution через index.spec.html
- Ресурс: https://github.com/STT-VITI-22/stt-pz-1
| RWP ✓ / DATASET(stt-pz-1, QALight: osnovi) / MODERN ✓ |
```

---

### 2.2 CHAPTER 9: ТЕСТУВАННЯ У AGILE/DEVOPS СЕРЕДОВИЩАХ

**Добавити новий підрозділ:**

```
| 9.7 Практичні завдання: TDD та BDD у современных методологіях |
- Проект stt-pz-2: TDD з Jest (>90% покриття)
- Проект stt-pz-4: BDD з Jest та spyOn mocking
- Integration з CI/CD pipeline
- Циклічний розвиток тестів та кода
- Достижение критеріїв acceptance
- Ресурси: https://github.com/STT-VITI-22/stt-pz-2, https://github.com/STT-VITI-22/stt-pz-4
| RWP ✓ / DATASET(stt-pz-2, stt-pz-4, QALight: osnovi/agile) / MODERN ✓ |
```

---

### 2.3 CHAPTER 11: ТЕХНІЧНІ ОСНОВИ ДЛЯ ТЕСТУВАЛЬНИКІВ

**Добавити новий підрозділ:**

```
| 11.7 Практичне завдання: API тестування та Mock дані |
- Проект stt-pz-3: API тестування з Jest
- Mock функції та дані для тестування
- Ice and Fire API приклад (books и houses endpoints)
- JSON структури та валідація
- Інструменти: Jest mock functions, axios/fetch mocking
- Ресурс: https://github.com/STT-VITI-22/stt-pz-3
| RWP ✓ / DATASET(stt-pz-3, QALight: zagalne/api) / MODERN ✓ |
```

---

### 2.4 CHAPTER 13: АВТОМАТИЗАЦІЯ ТЕСТУВАННЯ

**Добавити новий підрозділ:**

```
| 13.7 Практичні завдання: Modern Test Automation |
- Проект stt-pz-5: End-to-End тестування з Cypress
- Cypress порівняно з Selenium/Playwright
- E2E test cases для веб-додатків
- Cypress best practices та patterns
- Browser automation и real user interactions
- Ресурс: https://github.com/STT-VITI-22/stt-pz-5
| RWP ✓ / DATASET(stt-pz-5, books_pdf) / MODERN ✓ |
```

---

### 2.5 CHAPTER 5: РІВНІ ТЕСТУВАННЯ

**Розширити розділ 5.5 "Інші рівні тестування":**

```
| 5.6 Практичне завдання: End-to-End тестування |
- Рівень: System/E2E
- Инструмент: Cypress
- Реальні сценарії взаємодії з браузером
- Проект stt-pz-5
- Acceptance criteria та user workflows
- Ресурс: https://github.com/STT-VITI-22/stt-pz-5
| RWP ✓ / DATASET(stt-pz-5) / MODERN ✓ |
```

---

### 2.6 CHAPTER 12: МЕТРИКИ ТА ОЦІНЮВАННЯ ЯКОСТІ (РОЗШИРЕНЕ)

**Добавити новий підрозділ 12.6:**

```
| 12.6 Практичне завдання: ELK + MCP AI Log Analysis 🆕 |
- Практичний проект stt-elk-mcp-logging
- ELK Stack deployment (Elasticsearch, Logstash, Kibana)
- Структуроване логування з Python/Node.js додатків
- Logstash pipelines для парсингу та збагачення логів
- Kibana dashboards: Performance, Errors, Traffic
- **MCP сервер для AI аналізу** (NEW)
- Claude API integration для детекції аномалій та RCA
- Anomaly detection та intelligent alerting
- Docker Compose full stack
- Ресурс: https://github.com/STT-VITI-22/stt-elk-mcp-logging
| RWP ✓ / DATASET(stt-elk-mcp-logging, practical_tasks, books_pdf) / MODERN ✓ |
```

**Важливість:** Цей розділ демонструє сучасний підхід до спостережуваності (observability) та моніторингу в production, з інноваційною інтеграцією AI для аналізу логів через MCP (Model Context Protocol).

---

## 3. ТЕХНІЧНА АРХІТЕКТУРА ПРАКТИЧНИХ ЗАВДАНЬ

### 3.1 Навчальна прогресія

```
Level 1: Основи (Foundation)
├── stt-pz-1: Unit тестування (Mocha/Chai)
└── stt-pz-2: TDD методологія (Jest)

Level 2: Середній (Intermediate)
├── stt-pz-3: API тестування (Jest + Mock)
└── stt-pz-4: BDD методологія (Jest + spyOn)

Level 3: Просунутий (Advanced)
└── stt-pz-5: E2E тестування (Cypress)

Capstone: Екзамен
└── exam: Комплексна контрольна робота
```

### 3.2 Технологічні стеки

| Проект | Фреймворк | Технології | Версія Node |
|--------|-----------|-----------|------------|
| stt-pz-1 | Mocha + Chai | JavaScript (Browser) | n/a |
| stt-pz-2 | Jest | JavaScript (Node.js) | ≥12 |
| stt-pz-3 | Jest | JavaScript + API mocking | ≥12 |
| stt-pz-4 | Jest | JavaScript/TypeScript | ≥14 |
| stt-pz-5 | Cypress | JavaScript (E2E) | ≥12 |

---

## 4. РЕКОМЕНДАЦІЇ ПО НАПОВНЕННЮ DATASET

### 4.1 Нова папка структура для практичних завдань

```
dataset/
├── practical_tasks/
│   ├── stt-pz-1-mocha-chai/
│   │   ├── README.md (опис проекту)
│   │   ├── src/
│   │   │   ├── lib.js (приклади кода для тестування)
│   │   │   └── lib.spec.js (приклади тестів)
│   │   ├── setup.md (інструкції налаштування)
│   │   └── best-practices.md (best practices)
│   │
│   ├── stt-pz-2-jest-tdd/
│   │   ├── README.md
│   │   ├── src/
│   │   │   ├── lib.js
│   │   │   └── lib.spec.js
│   │   ├── jest.config.js (приклад конфігурації)
│   │   └── coverage-examples.md (примеры покриття)
│   │
│   ├── stt-pz-3-jest-api/
│   │   ├── README.md
│   │   ├── src/
│   │   │   ├── api.js
│   │   │   └── api.spec.js
│   │   ├── mock-data/
│   │   │   ├── books.json (Ice and Fire API books)
│   │   │   └── houses.json (houses data)
│   │   └── mocking-strategies.md
│   │
│   ├── stt-pz-4-jest-bdd/
│   │   ├── README.md
│   │   ├── libs/
│   │   │   ├── Calculator.ts
│   │   │   └── Calculator.spec.js
│   │   ├── spy-examples.md (spyOn examples)
│   │   └── bdd-patterns.md
│   │
│   └── stt-pz-5-cypress-e2e/
│       ├── README.md
│       ├── cypress/
│       │   ├── e2e/
│       │   │   ├── calculator.spec.cy.js
│       │   │   └── user-workflows.spec.cy.js
│       │   ├── support/
│       │   └── fixtures/ (тестові дані)
│       ├── cypress.config.js
│       └── e2e-patterns.md
│
└── frameworks_comparison/
    ├── mocha-vs-jest.md
    ├── jest-vs-cypress.md
    ├── testing-pyramid.md
    └── tool-selection-guide.md
```

### 4.2 Рекомендовані матеріали для додавання у dataset

#### 4.2.1 Для stt-pz-1 (Mocha/Chai)

**Файли для додавання:**
- `dataset/practical_tasks/stt-pz-1-mocha-chai/mocha-chai-tutorial.md` — виведення Mocha та Chai
- `dataset/practical_tasks/stt-pz-1-mocha-chai/browser-testing-guide.md` — тестування в браузері
- `dataset/practical_tasks/stt-pz-1-mocha-chai/bdd-vs-tdd.md` — порівняння BDD та TDD

**Вміст документів:**
```markdown
# Mocha та Chai Tutorial

## Основні концепції
- Describe blocks (test suites)
- It blocks (test cases)
- Before/After hooks
- Assertion styles (expect, should, assert)

## Практичні приклади
- Simple function testing
- Async testing (callbacks, promises)
- Error testing

## Best Practices
- Test organization
- Naming conventions
- Test isolation
```

#### 4.2.2 Для stt-pz-2 (Jest TDD)

**Файли для додавання:**
- `dataset/practical_tasks/stt-pz-2-jest-tdd/jest-configuration.md` — конфігурація Jest
- `dataset/practical_tasks/stt-pz-2-jest-tdd/tdd-workflow.md` — TDD робочий цикл
- `dataset/practical_tasks/stt-pz-2-jest-tdd/coverage-analysis.md` — аналіз покриття

**Вміст документів:**
```markdown
# Jest TDD Workflow

## Red-Green-Refactor Цикл
1. RED: Написати тест, який падає
2. GREEN: Написати код, щоб тест пройшов
3. REFACTOR: Поліпшити код, зберігаючи тест зеленим

## Jest Features
- describe() - test suites
- test() / it() - test cases
- expect() - assertions
- beforeEach() / afterEach() - hooks
- .toEqual(), .toBe(), .toThrow() - matchers

## Coverage Goals
- Line coverage: 90%+
- Branch coverage: 80%+
- Function coverage: 90%+
```

#### 4.2.3 Для stt-pz-3 (Jest API)

**Файли для додавання:**
- `dataset/practical_tasks/stt-pz-3-jest-api/api-testing-strategies.md` — стратегії API тестування
- `dataset/practical_tasks/stt-pz-3-jest-api/mock-data-management.md` — управління mock даними
- `dataset/practical_tasks/stt-pz-3-jest-api/ice-and-fire-api-docs.md` — документація API

**Вміст документів:**
```markdown
# API Testing with Jest

## Mock Functions
- jest.fn() - create mock functions
- jest.mock() - mock modules
- jest.spyOn() - spy on methods

## Mock Data
- fixtures -預設дані
- factory functions - динамічне створення даних
- faker libraries - генерація реалістичних даних

## API Testing Patterns
- Mocking fetch/axios
- Testing request/response cycles
- Error handling
- Async/await testing
```

#### 4.2.4 Для stt-pz-4 (Jest BDD)

**Файли для додавання:**
- `dataset/practical_tasks/stt-pz-4-jest-bdd/bdd-methodology.md` — BDD методологія
- `dataset/practical_tasks/stt-pz-4-jest-bdd/spyOn-advanced.md` — spyOn техніки
- `dataset/practical_tasks/stt-pz-4-jest-bdd/gherkin-examples.md` — Gherkin синтаксис

**Вміст документів:**
```markdown
# BDD Testing with Jest

## BDD Philosophy
- Write tests from business perspective
- Given-When-Then structure
- Executable specifications

## Jest BDD Features
- describe blocks as feature
- test cases as scenarios
- clear assertion messages

## spyOn Examples
- Spying on functions
- Asserting function calls
- Verifying call arguments
- Mocking return values
```

#### 4.2.5 Для stt-pz-5 (Cypress E2E)

**Файли для додавання:**
- `dataset/practical_tasks/stt-pz-5-cypress-e2e/cypress-fundamentals.md` — основи Cypress
- `dataset/practical_tasks/stt-pz-5-cypress-e2e/e2e-testing-patterns.md` — E2E паттерни
- `dataset/practical_tasks/stt-pz-5-cypress-e2e/real-user-workflows.md` — реальні користувацькі сценарії

**Вміст документів:**
```markdown
# Cypress E2E Testing

## Cypress vs Selenium
- Single process vs separate server
- Same JavaScript context
- Better debugging
- Real user interactions

## Cypress Commands
- cy.visit() - navigate
- cy.get() - element selection
- cy.type() - user input
- cy.click() - user click
- cy.should() - assertions

## Test Scenarios
- User registration flow
- Login/logout workflows
- Form submissions
- Error handling
```

### 4.2.6 Порівняльні документи

**Файли для додавання:**

1. `dataset/frameworks_comparison/testing-frameworks-overview.md`
```markdown
# Тестові фреймворки — Повний огляд

| Аспект | Mocha | Jest | Cypress |
|--------|-------|------|---------|
| Тип | Unit/Component | Unit/API | E2E |
| Мова | JavaScript | JavaScript | JavaScript |
| Конфігурація | Зовнішня | Вбудована | Вбудована |
| Асинхронність | Callback/Promise | Native | Native |
|성능 | Хороша | Очень добра | Задовільна |
| Документація | Хороша | Відмінна | Відмінна |
```

2. `dataset/frameworks_comparison/testing-pyramid.md`
```markdown
# Testing Pyramid

          △
         /|\
        / | \
       /  |  \ E2E Testing (10%)
      /   |   \ Cypress, Selenium
     /____|____\
    /     |     \
   /      |      \ Integration Testing (30%)
  /       |       \ Jest API, API testing
 /________|________\
/         |         \
Unit Testing (60%)    \
Mocha, Jest, etc.     \
```

3. `dataset/frameworks_comparison/tool-selection-guide.md`
```markdown
# Вибір інструментів тестування

## Коли використовувати:

### Unit Testing
- Mocha: для браузерних додатків
- Jest: для Node.js та React
- Обов'язковий мінімум покриття: 80%

### API Testing
- Jest з mock функціями
- REST Assured (Java)
- Postman

### E2E Testing
- Cypress: для сучасних веб-додатків
- Selenium: для legacy додатків
- Pupeteef: для headless тестування

### Performance Testing
- k6, JMeter, LoadRunner
```

---

## 5. ІНТЕГРАЦІЯ З ІСНУЮЧОЮ СТРУКТУРОЮ

### 5.1 Посилання у HANDBOOK_STRUCTURE.md

**Додати у відповідні розділи:**

```
✅ Chapter 7.8 — посилання на stt-pz-1
✅ Chapter 9.7 — посилання на stt-pz-2, stt-pz-4
✅ Chapter 11.7 — посилання на stt-pz-3
✅ Chapter 13.7 — посилання на stt-pz-5
✅ Chapter 5.6 — посилання на stt-pz-5

+ Nuevo: "Practical Tasks Index" сторінка, яка посилається на всі завдання
```

### 5.2 Оновлення CLAUDE.md

**Додати розділ про практичні завдання:**
```
## Розділ 8: Практичні Завдання та Проекти

8.1 Структура практичних завдань
8.2 GitHub интеграция (stt-pz-1 до stt-pz-5)
8.3 Dataset посилання на завдання
8.4 Реалізація посилань у HANDBOOK
```

### 5.3 Оновлення CHANGELOG.md

```markdown
### Added / Додано
- **PRACTICAL_TASKS_INTEGRATION.md** — інтеграція практичних завдань
- Новий розділ "Практичні завдання" у HANDBOOK_STRUCTURE.md:
  * 7.8 Unit тестування з Mocha/Chai
  * 9.7 TDD та BDD у Agile/DevOps
  * 11.7 API тестування та Mock дані
  * 13.7 Modern Test Automation
  * 5.6 End-to-End тестування
- Нова папка структура в dataset/ для практичних завдань
- Рекомендовані матеріали для додавання у dataset
```

---

## 6. ПРОПОЗИЦІЯ ЗМІСТУ ДЛЯ ПРАКТИЧНИХ ЗАВДАНЬ

### 6.1 Структура на рівні посібника

**Додати новий розділ перед закриттям кожної частини:**

```
### ПРАКТИЧНІ ЗАВДАННЯ

На закінчення цієї частини, виконайте практичні завдання:

PART I → stt-pz-1 (Unit Testing Basics)
PART II → stt-pz-2 (TDD Methodology)
PART III → stt-pz-3 (API Testing)
PART III → stt-pz-4 (BDD Methodology)
PART IV → stt-pz-5 (E2E Testing)
```

### 6.2 Format інструкцій у посібнику

```markdown
## Практичне завдання: [Назва]

**GitHub:** https://github.com/STT-VITI-22/[repo]
**Тип тестування:** [Unit/API/E2E]
**Фреймворк:** [Mocha/Jest/Cypress]
**Тривалість:** [кількість годин]
**Рівень складності:** [Beginner/Intermediate/Advanced]

### Мета завдання
[1-2 речення про мету]

### Чого ви навчитесь
- Концепція 1
- Концепція 2
- Концепція 3

### Вимоги успіху
- Критерій 1
- Критерій 2
- Критерій 3 (наприклад, >90% покриття)

### Кроки виконання
1. Клонуйте репозиторій
2. Встановіть залежності
3. Напишіть тести
4. Реалізуйте функцію
5. Перевірте покриття

### Посилання на матеріали
- [Посилання 1]
- [Посилання 2]
```

---

## 7. ДАТА-ПЛАН ІМПЛЕМЕНТАЦІЇ

### Фаза 1: Планування (завершено)
- ✅ Аналіз практичних завдань
- ✅ Визначення відповідності до глав посібника
- ✅ Розроблення структури dataset

### Фаза 2: Інтеграція (наступні кроки)
- [ ] Оновлення HANDBOOK_STRUCTURE.md з посиланнями на практичні завдання
- [ ] Створення папки practical_tasks/ у dataset/
- [ ] Додавання матеріалів до dataset/ для кожного проекту
- [ ] Оновлення CLAUDE.md з правилами для практичних завдань
- [ ] Оновлення CHANGELOG.md

### Фаза 3: Документація
- [ ] Написання інструкцій для кожного завдання
- [ ] Создание "Практичні завдання" індекс сторінки
- [ ] Додавання обов'язкових ресурсів до dataset/

### Фаза 4: Контроль якості
- [ ] Перевірка всіх посилань на GitHub
- [ ] Тестування структури dataset
- [ ] Перевірка консистентності з HANDBOOK структурою

---

## 8. ЗАКЛЮЧНЫЕ РЕКОМЕНДАЦІЇ

### 8.1 Best Practices

1. **Посилання на GitHub:** Завжди використовуйте прямі посилання на репозиторії та конкретні файли
2. **Версіонування:** Документуйте версії фреймворків, що використовуються
3. **Локалізація:** Готуйте матеріали як на українській так і на англійській мовах
4. **Обслуговування:** Регулярно перевіряйте посилання на GitHub на актуальність

### 8.2 Потенціальні розширення

- Додавання практичних завдань для Embedded/IoT тестування (Chapters 17-22)
- Інтеграція з CI/CD (GitHub Actions для автоматизації тестів)
- Контейнеризація (Docker) для простої розробки
- Video tutorials для кожного завдання

### 8.3 Інтеграція з ISTQB v4.0

Всі практичні завдання вивчають тестування, узгоджене з ISTQB v4.0 стандартами:
- Unit тестування (Level 1: Foundation)
- API тестування (Level 2: Advanced)
- E2E тестування (Level 2: Advanced)
- BDD/TDD підходи (Agile специфікація)

---

## 9. ДЕТАЛІ НОВИХ ПРАКТИЧНИХ ЗАВДАНЬ (stt-manual-testing & stt-bug-reporting)

### 9.1 stt-manual-testing: Manual Testing & Test Case Design

**GitHub:** https://github.com/STT-VITI-22/stt-manual-testing
**Розділ посібника:** Chapter 3.6 "Процеси та цикли тестування"
**Рівень складності:** Beginner/Intermediate
**Тривалість:** 2-3 тижні
**Тип:** Manual Testing

#### Мета завдання
Навчити студентів створювати якісні тест-кейси та виконувати manual testing, розуміючи структуру, найменування та документування тестових сценаріїв.

#### Чого ви навчитесь
- Структура Test Case (ID, Title, Prerequisites, Steps, Expected Results, Actual Results)
- Позитивне та негативне тестування
- Граничні значення та еквівалентне розділення у практиці
- Документування test cases у спілках/Excel/JIRA
- Test Execution та запис результатів
- Різниця між Test Case та Test Scenario
- Best practices в написанні test cases

#### Вимоги успіху
- ✅ Написати 20+ test cases для реального додатку
- ✅ Охопити позитивне та негативне тестування
- ✅ Виконати manual testing та записати результати
- ✅ Задокументувати найменше 5 дефектів
- ✅ Створити RTM (Requirements Traceability Matrix)

#### Структура проекту
```
stt-manual-testing/
├── README.md (інструкції)
├── requirements/ (вимоги до додатку)
│   └── application-spec.md
├── test-cases/
│   ├── test-cases-template.xlsx (шаблон)
│   ├── TC_001_UserLogin.md
│   ├── TC_002_UserRegistration.md
│   └── ... (20+ test cases)
├── test-execution/
│   ├── test-execution-report.xlsx
│   └── results/
├── defect-reports/
│   ├── BUG_001_LoginFailed.md
│   └── ... (defect reports)
├── rtm/
│   └── requirements-traceability-matrix.xlsx
└── datasets/
    └── test-data.xlsx
```

#### Матеріали для dataset
- `test-case-template.md` — шаблон для написання test cases
- `test-case-best-practices.md` — найкращі практики
- `positive-negative-testing.md` — позитивне та негативне тестування
- `boundary-value-testing.md` — граничне тестування
- `rtm-guide.md` — створення RTM

---

### 9.2 stt-bug-reporting: Bug Reporting & Defect Management

**GitHub:** https://github.com/STT-VITI-22/stt-bug-reporting
**Розділ посібника:** Chapter 8.7 "Управління дефектами"
**Рівень складності:** Beginner/Intermediate
**Тривалість:** 2-3 тижні
**Тип:** Manual Testing + Defect Management

#### Мета завдання
Навчити студентів як правильно документувати дефекти, класифікувати їх та управляти життєвим циклом дефекту в JIRA/Bugzilla системах.

#### Чого ви навчитесь
- Структура Bug Report (ID, Title, Description, Steps to Reproduce, Expected vs Actual Result)
- Класифікація дефектів (Severity: Critical/Major/Minor/Trivial, Priority: High/Medium/Low)
- Bug Report в JIRA (створення, редагування, посилання на вимоги)
- Життєвий цикл дефекта (New → Open → Assigned → In Progress → Fixed → Verified → Closed)
- Root Cause Analysis (RCA) для критичних дефектів
- Комунікація дефектів з розробниками
- Тестування fix-а та верифікація
- Best practices в bug reporting

#### Вимоги успіху
- ✅ Створити 15+ bug reports для реального додатку
- ✅ Правильно класифікувати дефекти за Severity та Priority
- ✅ Виконати RCA для 3+ критичних дефектів
- ✅ Задокументувати життєвий цикл 10+ дефектів
- ✅ Виконати retesting для 5+ fixed дефектів
- ✅ Створити дефект-метрики (Defect Density, Escape Rate)

#### Структура проекту
```
stt-bug-reporting/
├── README.md (інструкції та посилання на JIRA)
├── jira-setup/
│   ├── jira-configuration-guide.md
│   ├── custom-fields.md
│   └── workflow-diagram.png
├── bug-reports/
│   ├── BUG_001_LoginPageTitle.md
│   ├── BUG_002_PasswordValidation.md
│   └── ... (15+ bug reports)
├── rca-analysis/
│   ├── RCA_001_CriticalBug.md
│   ├── RCA_template.md
│   └── ... (RCA for critical bugs)
├── test-data/
│   ├── application-with-bugs.exe (або посилання)
│   └── test-users.xlsx
├── metrics/
│   ├── defect-metrics.xlsx
│   ├── defect-density.md
│   └── defect-distribution.png
└── templates/
    ├── bug-report-template.md
    ├── rca-template.md
    └── severity-priority-guide.md
```

#### Матеріали для dataset
- `bug-report-template.md` — шаблон для написання bug report
- `severity-priority-classification.md` — класифікація за важливістю
- `rca-methodology.md` — методологія RCA
- `jira-for-bug-reporting.md` — навіч користуватися JIRA
- `bug-reporting-best-practices.md` — найкращі практики
- `defect-lifecycle.md` — опис життєвого циклу дефекту
- `defect-metrics-analysis.md` — аналіз дефект-метрик
- `communication-templates.md` — шаблони комунікації з розробниками

---

### 9.3 Навчальна прогресія (Оновлена)

```
┌─────────────────────────────────────────────────┐
│ FOUNDATION PHASE (Частина I)                    │
├─────────────────────────────────────────────────┤
│ stt-manual-testing (Ch 3.6)                     │
│ → Розуміння основ manual testing                │
│ → Створення test cases                          │
│ → Test Execution та документування              │
└─────────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────┐
│ CORE TESTING PHASE (Частина II)                 │
├─────────────────────────────────────────────────┤
│ stt-pz-1 (Ch 7.8): Unit Testing (Mocha/Chai)   │
│ stt-bug-reporting (Ch 8.7): Bug Reporting      │
│ → Техніки тестування                            │
│ → Manual дефект-документування                  │
└─────────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────┐
│ ADVANCED AUTOMATION (Частина III-IV)            │
├─────────────────────────────────────────────────┤
│ stt-pz-2 (Ch 9.7): TDD (Jest)                   │
│ stt-pz-3 (Ch 11.7): API Testing (Jest)          │
│ stt-pz-4 (Ch 9.7): BDD (Jest)                   │
│ stt-pz-5 (Ch 13.7): E2E Testing (Cypress)       │
│ → Автоматизовані test фреймворки                │
│ → Modern QA практики                            │
└─────────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────┐
│ CAPSTONE: exam (Комплексна контрольна робота)  │
│ → Поєднання усіх навичок                        │
└─────────────────────────────────────────────────┘
```

---

**Статус:** ГОТОВО ДО ІМПЛЕМЕНТАЦІЇ
**Слідуючі кроки:** Оновлення HANDBOOK_STRUCTURE.md та додавання матеріалів у dataset/
**НОВИНКИ:** Додані stt-manual-testing та stt-bug-reporting для повного покриття manual testing
