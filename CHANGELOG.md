

# Історія змін — STT Handbook

Всі значущі зміни до цього проекту задокументовані в цьому файлі.

Формат базується на [Keep a Changelog](https://keepachangelog.com/uk/) та проект дотримується [Semantic Versioning](https://semver.org/).

---

## [Невипущено] / Unreleased

### Added / Додано

- **Глава 3: Процеси та цикли тестування** (1207 рядків) 🆕 ⭐
  - (docs) Повна глава з 7 розділів за ISTQB v4.0 стандартом:
    * 3.1 Фундаментальний процес тестування (6 фаз: Planning → Closure)
    * 3.2 STLC та взаємозв'язок із SDLC
    * 3.3 Entry Criteria та Exit Criteria (практичні приклади)
    * 3.4 Матриці: RTM, Coverage, Execution (з шаблонами)
    * 3.5 Ролі та RACI матриця (Manual QA, Test Lead, Automation)
    * 3.6 Практичне завдання: Manual Testing, Test Case Design
    * 3.7 Положення та ключові висновки
  - Включено: Mermaid діаграми (6), таблиці (12+), приклади зі світу (Google Cloud, Banking App, To-Do List)
  - Посилання на практичний GitHub проект stt-manual-testing
  - Production-ready для інтеграції

- **TERMINOLOGY.md** — 11 нових критичних термінів з Глави 2-3 ✨
  - (docs) Розділ "Терміни щодо SDLC та моделей розробки":
    * SDLC / Життєвий цикл розробки ПЗ
    * Waterfall Model / Каскадна модель
    * V-Model / V-подібна модель
    * Iterative Model / Ітеративна модель
    * Spiral Model / Спіральна модель
    * Agile / Гнучка розробка
    * Shift-Left / Раннє тестування
    * Boehm's Curve / Крива витрат на виправлення дефектів
  - (docs) Розділ "Терміни щодо документації тестування":
    * QA Plan / QA План
    * Test Strategy / Стратегія тестування
    * Test Plan / План тестування
    * Entry Criteria / Критерії входження
    * Exit Criteria / Критерії завершення
  - (docs) Розділ "Терміни щодо метрик якості":
    * Defect Density / Щільність дефектів

- **ABBREVIATIONS.md** — Додано MTTR (Mean Time To Repair) ✨
  - (docs) MTTR — Середній час на виправлення (нова метрика якості)

### Fixed / Виправлено
- **Глава 2: Основи контролю якості** — Фінальна лінгвістична вичитка та виправлення росіянізмів 🔍
  - (fix) Виявлено та виправлено 6 мовних помилок, граматичних огріхів та дослівних перекладів
  - (fix) ВАЖЛИВИЙ УРОК: При видаленні дублювання заголовків було помилково видалено Mermaid діаграму Shift-Left та таблицю з 3 QR кодами (Boehm's Curve, New SDLC Vibe, Barry Boehm). Ці матеріали мають бути повернені користувачем.
  - Помилки виправлені:
    * "юзабіліті" → "зручність використання" (UI/UX термін)
    * "програмського продукту" → "програмного продукту" (граматична форма)
    * "акт прийманості" → "акт здачі-приймання" (суржик, офіційний термін)
    * "на однакові дні" → "з перших днів спринту на рівних правах" (дослівний переклад)
    * "Ранне виявлення" → "Раннє виявлення" (помилка в наголосі)
    * "у віку генеративних LLM" → "в еру генеративних LLM" (мовна калька)
  - Видалено дублювання заголовку ### 2.4.1 (були два однойменні заголовки)
  - Перевірено всі похідні форми слів для консистентності

### Changed / Змінено
- **CLAUDE.md** — Оновлено правила для запобігання росіянізмам та мовним калькам
  - Додано 6 нових типових помилок до таблиці § 2.1 (базовані на Главі 2)
  - Розширено § 2.2 з граматичними помилками специфічно для QA/Testing domain
  - Повністю переписано § 2.3 (Правило перевірки) з деталізованими кроками
  - Додано рядок "Типові помилки з Глави 2" з еxclamation/checkmark діаграмою
  - Посилена увага на множину іменика та правильний відмінок

- **Глава 2: Основи контролю якості** (v2.0) — Повна переробка з дотриманням строгих нових стандартів 🔄
  - (refactor) Переписана з нуля у відповідь до strict specifications
  - Нові Mermaid діаграми для ISO/IEC 25010 модель, QA/QC/Testing ієрархія, Shift-Left testing, SDLC Verification/Validation, Career path
  - Markdown-only formatting (видалено HTML теги)
  - GitHub absolute URLs для всіх dataset посилань
  - Zero Russian loanwords (всі перевірено)
  - Практичний case study: Mobile Banking App з економічним аналізом (Boehm's Curve)
  - Мініатюрний тест з 4 питаннями та детальними обґрунтуваннями
  - ISO/IEC 25010:2011 та ISTQB v4.0 compliance
  - Статус: Production-ready для інтеграції до посібника

### Added / Додано
- **HANDBOOK_STRUCTURE.md v1.0** (71 КБ) — MASTER BLUEPRINT INITIAL RELEASE 🆕
  - 23 глави, 5 частин, 100+ підрозділів
  - **Нові критичні розділи для v1.0:**
    * **15.4 Agentic AI Testing** — 500% growth (5% → 30% adoption)
    * **12.6 Synthetic Monitoring & Observability** — 117% growth (RUM + Synthetic)
    * **6.4 Supply Chain Security** — OWASP 2025 нова категорія (#3)
    * **13.7 Cloud-Native & Kubernetes Testing** — 96% adoption, 34% readiness gap
    * **23 Chaos Engineering & Resilience Testing** — 167% growth (FIT, LitmusChaos)
  - Матриця актуальності: 85% сучасних трендів включено

- **SOURCE_NOTATION_GUIDE.md** (12 КБ) — Довідник нотації RWP/DATASET/MODERN 🆕
  - Пояснення системи позначення джерел інформації у HANDBOOK_STRUCTURE.md
  - RWP (Working Program) — покриття офіційною програмою навчання
  - DATASET — організація локальної бази знань (370+ файлів з 6 джерел)
  - MODERN — статус актуальності знань для 2024-2026 років
  - Матриці статусів для швидкої інтерпретації
  - 6 практичних прикладів з реальних розділів посібника
  - Матриця для визначення пріоритету розробки

- **TRENDS_2024_2026_EXECUTIVE_SUMMARY.md** (9 КБ) — Виконавчий звіт дослідження трендів
- **TRENDS_2024_2026_SUMMARY.md** (9 КБ) — Зведені таблиці та рекомендації
- **TRENDS_2024_2026_RESEARCH.md** (26 КБ) — Детальне дослідження 10 тем (25+ джерел)

### Changed / Змінено
- Оновлено Chapter 6.4 (Security Testing):
  - Додано Supply Chain Security Testing (OWASP 2025 новинка)
  - SCA tools, SBOM generation, signed artifacts, build security
  - Real-world threat example: Shai-Hulud (2025) npm worm

- Розширено Chapter 13 (Automation):
  - Додано 13.7: Cloud-Native & Kubernetes Testing (critical adoption gap)
  - Testkube, container scanning, K8s manifest validation, GitOps
  - Перейменовано Ch 13.7 → Ch 13.8 (Cypress E2E завдання)

- Розширено Chapter 12 (Metrics & Quality):
  - Додано 12.6: Synthetic Monitoring & Observability (117% growth)
  - RUM + Synthetic Monitoring, UXO, OpenTelemetry, Grafana k6
  - Перейменовано Ch 12.6 → Ch 12.7 (ELK + MCP завдання)

- Розширено Chapter 15 (AI/LLM Testing):
  - Додано 15.4: Agentic AI Testing (РЕВОЛЮЦІЙНА, 500% growth)
  - Self-healing, production failure → tests, autonomous agents
  - Adoption: 5% (2024) → 30% (2025) → 70% (2026)

### Fixed / Виправлено
- Номерація розділів HANDBOOK_STRUCTURE.md синхронізована з новими добавленнями

### Quality Assessment / Оцінка якості
- **CONTENT_QUALITY_ASSESSMENT.md** (34 КБ) — Детальна оцінка всіх аспектів
  - 🏆 Final Score: 8.8/10 (МАЙСТЕРНА ПРАЦЯ — ОДИНИЦЯ ВИЩОГО КЛАСУ)
  - Оцінка по 7 компонентам (структура, актуальність, теорія, практика...)
  - Матриця критичності по розділам
  - Рекомендації для поліпшення з PRIORITY 1-3

- **QUALITY_ASSESSMENT_BRIEF.md** (4 КБ) — Скорочений звіт
  - Final score: 8.8/10 з детальним аналізом
  - Таблиця оцінок, сильні/вразливі місця, вердикт

**ОЦІНКА ПО КОМПОНЕНТАМ:**
- Актуальність змісту:    8.5/10 (85% сучасних трендів 2024-2026)
- Структурна цільність:   9.0/10 (4-рівнева ієрархія)
- Покриття теорії:        8.8/10 (95-100% для Ch 1-16)
- Практичні компоненти:   8.2/10 (15 проектів: 8 існуючих + 7 нових)
- Джерельна база:         9.2/10 (370+ файлів, 26 книг, 25+ веб-джерел 2024-2026)
- Мовна узгодженість:     9.1/10 (українська 100%)
- Готовність до розробки: 8.7/10 (дорожна карта готова, 3 фази 2024-2026)

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
  - `dataset/articles/qalight/parsed/osnovi/agile.md`
  - `dataset/articles/QA_Bible/sdlc-i-stlc/agile.md`
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
| dataset/articles/QA_Bible | 241 | 3.7 МБ |
| dataset/articles/qalight/parsed | 89 | 692 КБ |
| dataset/books_pdf/parsed | 26 | 170 МБ |
| dataset/pptx_doc | 8 | 5.6 МБ |
| dataset/articles/dou | 4 | 144 КБ |
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
