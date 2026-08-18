

# Історія змін — STT Handbook

Всі значущі зміни до цього проекту задокументовані в цьому файлі.

Формат базується на [Keep a Changelog](https://keepachangelog.com/uk/) та проект дотримується [Semantic Versioning](https://semver.org/).

---

## [Невипущено] / Unreleased

### Added / Додано
- **HANDBOOK_STRUCTURE.md v2.0** (95 КБ) — MASTER BLUEPRINT розширеної структури посібника 🆕
  - Розширено з 16 на 22 глави + 5 частин
  - Структура: 5 основних частин + 22 розділи + 80+ підрозділів
  - Нова PART V: Embedded QA, IoT, DefTech (Chapters 17-22)
  - Оновлено глави 15-16: AI/LLM Testing та Career/Certifications
  - Матриця відстежуваності RWP → Dataset → ISTQB 4.0 → Modern Knowledge
  - Верифікація: Chapters 1-16 (95-100% покриття), Chapters 17-22 (30-50% покриття)

- **CONTENT_VERIFICATION_REPORT.md** (55 КБ) — Детальна верифікація структури 🆕
  - Аналіз покриття для всіх 22 глав
  - Матриця покриття по датасету (370 файлів)
  - Gap analysis та рекомендації по розширенню
  - План розробки по версіях (v0.2-v1.1)
- **Керуючий граф програми (Control Flow Graph - CFG)** — детальне вивчення у розділах 7.1 та 12.2 🔄
  - Додано до HANDBOOK_STRUCTURE.md (Chapter 7.1 "Білий ящик тестування"):
    * Графічне представлення потоку управління
    * Вузли та ребра, базові блоки коду
    * Характеристики CFG та застосування у тестуванні
  - Додано до HANDBOOK_STRUCTURE.md (Chapter 12.2 "Метрики покриття тестування"):
    * CFG та його застосування для розрахунку кількості тестів
    * Незалежні шляхи в графі
  - Джерела: QA_Bible (test-dizain/static-static-analysis), books_pdf (Copeland 2004, Avramenko 2017, Didkovska 2011)
- **Цикломатична складність (McCabe Complexity)** — додано до розділів 7.1 та 12.2 🔄
  - Метрика складності коду на основі CFG
  - Формула: M = E − N + 2P (Е = ребра, N = вузли, P = компоненти)
  - Застосування при розробці та тестуванні
  - Рекомендовані межі складності (≤10)
- **Дослідження метрики "Майбета"** — аналіз проведено, документовано результати 🔍
  - Пошук у датасеті: не знайдено прямих посилань на "Майбета" (Maybeta)
  - Можливі варіанти:
    * Бетті число (Betti number) — топологічна метрика графів, згадана у статті про CFG
    * McCabe Complexity (цикломатична складність) — найбільш використовується метрика складності
    * Інші метрики складності: метрика Холстеда, метрика Чепіна, метрика Джилба
  - Рекомендація: уточнити термін з користувачем або замінити на "Цикломатична складність"
  - Метрики складності детально документовані у books_pdf (Hrytsiuk 2018)

- **Практичні завдання з тестування (8 проектів)** — інтеграція у структуру посібника 🎓
  - **PRACTICAL_TASKS_INTEGRATION.md** — розширена документація (v2.1)
  - Додано 2 нові практичні завдання для manual testing:
    * **stt-manual-testing** (Ch 3.6): Manual Testing & Test Case Design
      - Створення 20+ test cases
      - Позитивне та негативне тестування
      - Test Execution та документування
      - Requirements Traceability Matrix (RTM)
    * **stt-bug-reporting** (Ch 8.7): Bug Reporting & Defect Management
      - 15+ bug reports з класифікацією
      - Root Cause Analysis (RCA)
      - Життєвий цикл дефекта у JIRA
      - Дефект-метрики та аналіз

  - Додано 1 новий продвинутий проект для моніторингу та AI аналізу:
    * **stt-elk-mcp-logging** 🆕 (Ch 12.6): ELK + MCP AI Log Analysis
      - ELK Stack deployment (Elasticsearch, Logstash, Kibana)
      - Структуроване логування з Python/Node.js додатків
      - Logstash pipelines для парсингу та збагачення логів
      - Kibana dashboards (Performance, Errors, Traffic)
      - **MCP сервер для AI-powered аналізу** (NEW INNOVATION)
      - Claude API integration для детекції аномалій та RCA
      - Anomaly detection та intelligent alerting
      - Docker Compose full stack з 7 лабораторними вправами

  - Оновлено HANDBOOK_STRUCTURE.md з 8 практичними завданнями:
    * Ch 3.6: stt-manual-testing
    * Ch 7.8: stt-pz-1 (Mocha/Chai Unit Testing)
    * Ch 8.7: stt-bug-reporting
    * Ch 9.7: stt-pz-2 (TDD) + stt-pz-4 (BDD)
    * Ch 11.7: stt-pz-3 (API Testing with Jest)
    * Ch 13.7: stt-pz-5 (E2E Testing with Cypress)
    * Ch 5.6: stt-pz-5 (E2E Testing)
    * Ch 12.6: stt-elk-mcp-logging (ELK + MCP AI) 🆕

  - Структура розширена з "exam" екзаменом як capstone проектом

  - **Нові файли за stt-elk-mcp-logging:**
    * stt-elk-mcp-logging-SPECIFICATION.md (400+ рядків) — детальна специфікація проекту
    * Dataset матеріали (рекомендації): docker-compose examples, Logstash pipelines, MCP tools templates, Claude prompts

- Методологія LEAN та Kanban до словника термінів
- Розширений Словник термінів (TERMINOLOGY.md) з 30+ критичними термінами
- Перелік скорочень (ABBREVIATIONS.md) з 80+ скорочень
- CHANGELOG.md для документування всіх змін

### Fixed / Виправлено
- Українська орфографія: "гібкість" → "гнучкість"

### Changed / Змінено
- Оновлено CLAUDE.md з посиланнями на TERMINOLOGY.md та ABBREVIATIONS.md
- Оновлено CLAUDE.md розділ 2 (Мова): додано детальні правила уникнення російських слів (розділи 2.1-2.2)
- Розширено розділ 8.6 "Інструменти управління дефектами": додано Trello та Worksection
- Виправлено російські, китайські та інші помилкові слова у HANDBOOK_STRUCTURE.md:
  * "Исчерпывающее тестирование" → "Вичерпне тестування"
  * "Белый ящик" → "Білий ящик"
  * "Жизненный цикл" → "Життєвий цикл" (замінено на "Життєвий" в усіх варіаціях)
  * "Visione di impresa e utenti" → "Визначення та сфера"
  * "Alpha и Beta" → "Alpha та Beta"
  * "из розробки" → "з розробки"
  * "Переиспользование" (російська) → "Повторне використання" (українська)
  * "维護" (китайська) → "обслуговування" (українська)
  * "Організація кодо" → "Організація коду" (опечатка)

### Dataset Information / Інформація про Dataset
- **Dataset дата оновлення:** 17 серпня 2026 року (August 17, 2026)
- **Розташування:** dataset/ (6 основних джерел: qalight, QA_Bible, books_pdf, pptx_doc, dou, youtube)
- **Загалом:** 370 файлів, 181 МБ

### Dataset Analysis / Аналіз Dataset
- QALight: 89 файлів, 692 КБ (13 категорій)
- QA_Bible: 240+ файлів, 3.7 МБ (14 категорій)
- books_pdf: 26 професійних текстів, 170 МБ (1999-2024)
- Покриття: 95-100% для глав 1-16, 30-50% для глав 17-22 (Embedded/IoT)

### Verification & Approval / Верифікація та затвердження
- **FINAL_APPROVAL_REPORT.md** (18 КБ) — Остаточна верифікація структури
  - Зведена звірка всіх 22 глав
  - Рекомендації по уточненню Ch 1-3 та Ch 17-20
  - Матриця затвердження (82/100 ГОТОВО)
  - Рішення: ГОТОВО ДО РОЗРОБКИ з умовами

**Статус верифікації:** ✅ ЗАВЕРШЕНО
**Дозвіл на розробку:** ✅ ЗАТВЕРДЖЕНО

---

## [0.1.0] - 2026-08-17

### Added / Додано

#### Документація проекту
- **CLAUDE.md** (16 КБ) — Детальні інструкції для роботи з проектом
  - 20 розділів з правилами та вимогами
  - Визначення критичних термінів для проекту
  - Процес роботи та Git-умови

- **TERMINOLOGY.md** (35 КБ) — Словник термінів для посібника
  - Критичні терміни (Software Testing, Verification, Validation)
  - Розрізнення Error vs Defect vs Failure
  - Терміни щодо рівнів, типів та технік тестування
  - Терміни білого/чорного/сірого ящику
  - Терміни щодо методологій розробки (LEAN, Kanban, Scrum)
  - 30+ термінів з прикладами та джерелами

- **ABBREVIATIONS.md** (48 КБ) — Перелік скорочень для посібника
  - Скорочення щодо типів та рівнів тестування (QA, QC, BVT, UAT)
  - Архітектурні скорочення (API, UI, UX, HTTP, SQL, JSON, XML)
  - Методологічні скорочення (SDLC, STLC, Agile, Scrum, CI/CD, TDD, BDD)
  - Управління дефектами (JIRA, Bugzilla, RTM)
  - Техніки тестування (BVA, ECP, DTT)
  - Стандарти (ISTQB, IEEE, ISO/IEC, DSTU)
  - Платформи та технології (Git, Docker, MCP)
  - 80+ скорочень з розшифровками та контекстом

#### Матеріали з dataset
- Аналіз керуючого графа програми (Control Flow Graph) з:
  - `dataset/books_pdf/parsed/Copeland_2004_SoftwareTestDesign.md` (Chapter 10)
  - `dataset/books_pdf/parsed/Didkovska_2011_SoftwareTestingCriteriaAndMethods.md`
  - 5 рівнів покриття (C0 до C∞)
  - Практичні приклади та діаграми

- Методологія LEAN та Kanban з:
  - `dataset/qalight/parsed/osnovi/agile.md`
  - `dataset/QA_Bible/sdlc-i-stlc/agile.md`
  - 5 принципів LEAN
  - 4 ключові концепції (Muda, Mura, Muri, JIT)
  - Система управління потоком (Kanban)
  - Концепція WIP Limit

### Removed / Видалено
- Посилання на "ABBREVIATIONS.md (буде створено)" з TERMINOLOGY.md (файл вже існує)

### Changed / Змінено
- Оновлено CLAUDE.md з посиланнями на нові файли терміналогії

### Fixed / Виправлено
- Українська орфографія в TERMINOLOGY.md: "гібкість" → "гнучкість"

---

## Статистика проекту

### Основні файли проекту

| Файл | Розмір | Вміст |
|------|--------|-------|
| CLAUDE.md | 16 КБ | 427 рядків, 20 розділів |
| TERMINOLOGY.md | 35 КБ | 677 рядків, 30+ термінів |
| ABBREVIATIONS.md | 48 КБ | 1200+ рядків, 80+ скорочень |
| WORK_HISTORY.md | 39 КБ | Історія розробки парсерів |
| **Всього** | **138 КБ** | **2300+ рядків** |

### Источники в dataset

| Джерело | Файлів | Розмір |
|---------|--------|--------|
| dataset/QA_Bible | 241 | 3.7 МБ |
| dataset/qalight/parsed | 89 | 692 КБ |
| dataset/books_pdf/parsed | 26 | 170 МБ |
| dataset/pptx_doc | 8 | 5.6 МБ |
| dataset/dou | 4 | 144 КБ |
| **Всього** | **369** | **181 МБ** |

### Терміни та скорочення

| Тип | Кількість |
|-----|-----------|
| Критичні терміни | 15 |
| Терміни щодо тестування | 30+ |
| Терміни щодо методологій | 10+ |
| Скорочення | 80+ |
| Джерел у dataset | 7 |

---

## Git комміти цієї версії

```
46b0002 - fix: correct Ukrainian spelling 'гібкість' to 'гнучкість'
2d4699e - docs: add LEAN and Kanban to terminology and abbreviations
da78556 - add Abb and Terminology
0f36faa - add CLAUDE.md
```

---

## Плани на майбутнє (Roadmap)

### Наступні версії

- [ ] **HANDBOOK_STRUCTURE.md** — Структура посібника з розділами
- [ ] **Перший пілотний розділ** — "Що таке тестування ПЗ?" з прикладами
- [ ] **Розділи про рівні тестування** — Unit, Integration, System, Acceptance
- [ ] **Розділи про типи тестування** — Functional, Performance, Security тощо
- [ ] **Розділи про техніки дизайну** — Eквівалентне розділення, BVA, DTT
- [ ] **Інструменти контролю якості** — Скрипти для перевірки термінологічної узгодженості
- [ ] **Індекс та кросс-посилання** — Навігація між розділами

---

## Ліцензія

Цей проект та всі матеріали посібника розповсюджуються для освітніх цілей.

---

## Як внести вклад

Якщо ви хотіли б внести вклад:

1. Перейдіть на GitHub та створіть Issue з описом змін
2. Дотримуйтесь правил з CLAUDE.md
3. Переконайтеся, що термінологія відповідає TERMINOLOGY.md
4. Оновіть CHANGELOG.md в розділі "[Невипущено]"
5. Зробіть pull request з описом змін

---

## Джерела

**Основні джерела матеріалів:**
- QALight (Ukrainian QA Education) — https://qalight.ua/
- QA Bible — GitBook база знань з тестування
- Profesional Books:
  - Copeland, L. (2004) — "A Practitioner's Guide to Software Test Design"
  - Didkovska, Y. (2011) — "Критерії та методи тестування ПЗ"
  - Kulikov, S. (2020, 2022) — "Software Testing Base Course"
  - Gregory, J., Crispin, L. (2014) — "Agile Testing"
  - Beizer, B. (2004) — "Black-Box Testing"

**Документація проекту:**
- CLAUDE.md — Правила роботи з посібником
- TERMINOLOGY.md — Словник термінів
- ABBREVIATIONS.md — Перелік скорочень
- WORK_HISTORY.md — Історія розробки парсерів

---

## Контакти

**Автор**: Andrii Zadvornyi (a.zadvornyi@gmail.com)

**Репозиторій**: https://github.com/[repo]/stt-handbook

---

**Дата створення**: 17 серпня 2026
**Остання оновлення**: 17 серпня 2026
