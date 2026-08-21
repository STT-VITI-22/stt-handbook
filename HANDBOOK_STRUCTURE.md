# HANDBOOK_STRUCTURE.md — Повна структура посібника «Теорія тестування ПЗ»

**Документ базується на глибокому аналізі трьох основних компонентів:**

### 1. **Working Program** (Робоча програма навчальної дисципліни)
   - Офіційна структура курсу та вимоги до навчання
   - Всі основні розділи відображені в Chapters 1-16 з покриттям 100%

### 2. **Dataset Sources** (370 файлів, 181 МБ, 6 основних джерел)
   - **QALight (89 файлів, 692 КБ)** — українські освітні матеріали, 13 категорій
   - **QA_Bible (240+ файлів, 3.7 МБ)** — глибокі матеріали з 14 категорій
   - **books_pdf (26 професійних книг, 170 МБ)** — класичні праці (1999-2024)
   - **pptx_doc (8 презентацій, 5.6 МБ)** — практичні навчальні матеріали
   - **dou (4 статті, 144 КБ)** — сучасні статті та тренди
   - **youtube** — відеоресурси та практичні демонстрації

### 3. **Сучасні стандарти та актуальність знань** (2024-2026)
   - **ISTQB v4.0 Syllabus** — міжнародний стандарт сертифікації (100% покриття)
   - **ISO/IEC 25010:2011** — стандарт якості ПЗ (Ch 2, 12)
   - **OWASP Top 10 (2025 актуалізація)** — з новою категорією Supply Chain Security
   - **Сучасні тренди тестування** — AI Testing, Chaos Engineering, Cloud-Native Testing (85% покриття 2024-2026)
   - **Emerging Technologies** — Agentic AI (5% → 30% → 70% growth), Synthetic Monitoring (30% → 85% adoption)

**Дата створення:** 17 серпня 2026 року
**Версія:** v1.0 (INITIAL RELEASE)
**Статус:** MASTER BLUEPRINT — Повна організаційна структура посібника

---

## 1. EXECUTIVE SUMMARY

Цей документ визначає **повну структуру навчального посібника з теорії тестування програмного забезпечення**, організованого в **5 основних частин**, **23 розділи**, та **100+ підрозділів** з прямою відстежуваністю до dataset джерел та сучасної знань у галузі.

### Методологія розробки структури

```
Working Program (RWP)
       +
Dataset Sources (369 файлів)
       +
ISTQB Standards v4.0
       +
Modern Testing Knowledge
       ↓
CONTENT AUDIT
       ↓
CONTENT SYNTHESIS & DEDUPLICATION
       ↓
TRACEABILITY MAPPING
       ↓
HIERARCHICAL STRUCTURE
```

### Ключові метрики структури

| Метрика | Значення | Характеристика |
|---------|----------|---------|
| **Основні частини** | 5 | Introduction, Fundamentals, Advanced, Modern Practice, Embedded/IoT |
| **Розділи** | 23 | З прямою відстежуваністю до Working Program |
| **Підрозділи** | 100+ | З детальним вмістом та практичними завданнями |
| **Практичні проекти** | 8+ | GitHub репозиторії з реальними сценаріями |
| **Dataset файлів** | 370 | 181 МБ з 6 основних джерел |
| **QALight матеріалів** | 89 | 692 КБ, 13 категорій, українська мова |
| **QA_Bible матеріалів** | 240+ | 3.7 МБ, 14 категорій, глибока теорія |
| **Професійних книг** | 26 | 170 МБ, період 1999-2024 |
| **Період літератури** | 25 років | Від основоположників до сучасних трендів |
| **Стандарти** | 3 | ISTQB 4.0, ISO/IEC 25010, OWASP 2025 |
| **Покриття Ch 1-16** | ✅ 95-100% | Основний контент повністю готовий до розробки |
| **Покриття Ch 17-22** | ⚠️ 30-50% | Embedded/IoT спеціалізація (потребує доповнення) |
| **Актуальність знань** | 85% | 2024-2026 тренди включені (Agentic AI, Chaos Eng, Synthetic Monitoring) |

---

## 2. АРХІТЕКТУРА ПОСІБНИКА

### 2.1  4-рівнева ієрархія структури

```
HANDBOOK (Посібник)
    │
    ├── ЧАСТИНА 1: Вступ та фундаментальні основи
    │    ├── Глава 1: Вступ до тестування
    │    ├── Глава 2: Основи контролю якості
    │    ├── Глава 3: Процеси та цикли тестування
    │    └── Глава 4: Психологія та принципи тестування
    │
    ├── ЧАСТИНА 2: Базова теорія тестування
    │    ├── Глава 5: Рівні тестування
    │    ├── Глава 6: Типи тестування
    │    ├── Глава 7: Техніки тестування та дизайн
    │    └── Глава 8: Управління дефектами
    │
    ├── ЧАСТИНА 3: Розширені теми
    │    ├── Глава 9: Тестування у Agile/DevOps середовищах
    │    ├── Глава 10: Управління тестуванням та планування
    │    ├── Глава 11: Технічні основи для тестувальників
    │    └── Глава 12: Метрики та оцінювання якості
    │
    ├── ЧАСТИНА 4: Сучасна практика та ШІ
    │    ├── Глава 13: Автоматизація тестування
    │    ├── Глава 14: Мобільне тестування
    │    ├── Глава 15: Тестування в еру ШІ та LLM моделей
    │    └── Глава 16: Кар'єра та сертифікація
    │
    └── ЧАСТИНА 5: Embedded QA, IoT та DefTech
         ├── Глава 17: Основи схемотехніки та мікроконтролерів
         ├── Глава 18: Протокольний аналіз та робота з обладнанням
         ├── Глава 19: Нефункціональні сценарії «заліза» та надійність
         ├── Глава 20: Автоматизація тестування прошивок (Firmware)
         ├── Глава 21: Мережевий IoT-рівень, Connectivity та поле
         └── Глава 22: Методологія RCA та звіти для заліза
```

---

## 3. ДЕТАЛЬНА СТРУКТУРА РОЗДІЛІВ

### ЧАСТИНА 1: ВСТУП ТА ФУНДАМЕНТАЛЬНІ ОСНОВИ

Цільова аудиторія: Новачки, студенти, люди, що переходять у QA

#### **Глава 1: ВСТУП ДО ТЕСТУВАННЯ ПРОГРАМНОГО ЗАБЕЗПЕЧЕННЯ**

**Мета:** Дати чітке визначення та розуміння, що таке тестування ПЗ в сучасному контексті

| Підрозділ | Зміст | Джерела (RWP/DATASET/MODERN) | Ресурси |
|-----------|-------|-----|----------|
| 1.1 Визначення тестування ПЗ | - Офіційні визначення ISTQB v4.0<br>- Процес дослідження та перевірки<br>- Різноманіття підходів до визначення | RWP ✓ / DATASET(QALight: osnovi/shcho-take-testuvannia) / MODERN(ISTQB 4.0) | ![QR: ISTQB Definition](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.istqb.org/downloads&margin=10) |
| 1.2 Чому тестування необхідне | - Економіка дефектів та вартість помилок<br>- Ризики неправильної роботи ПЗ<br>- Скорочення часу вихідного продукту | RWP ✓ / DATASET(QALight: osnovi/chomu-testuvannia-neobkhidne, QA_Bible: obshee) / MODERN ✓ | ![QR: Boehm's Curve](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Software_testing&margin=10) |
| 1.3 Розповсюджені міфи про тестування | - Тестування гарантує якість? (Ні)<br>- Тестування знаходить ВСІ дефекти? (Ні)<br>- Тестування затримує розробку? (Залежить) | RWP ✓ / DATASET(QALight: osnovi/mifi-pro-testuvannia) / MODERN ✓ | ![QR: Testing Myths](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi/mifi-pro-testuvannia&margin=10) |
| 1.4 Еволюція тестування ПЗ | - Історія від 1999 року (Kaner)<br>- Розвиток техник та методів<br>- Сучасні тренди (AI, DevOps, Agile) | RWP ✓ / DATASET(books_pdf: Kaner 1999, Kulikov 2020-2022) / MODERN ✓ | ![QR: Testing History](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://github.com/STT-VITI-22/stt-handbook&margin=10) |
| 1.5 Тестування як професія | - Роль тестувальника в команді<br>- Відповідальність та компетенції<br>- Кар'єрні траєкторії | RWP ✓ / DATASET(QALight: osnovi/khto-zaimaietsia-testuvanniam, QA_Bible: faq-dlya-novichkov) / MODERN ✓ | ![QR: QA Career Path](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://dou.ua/qa-roadmap&margin=10) |

**Практичні приклади:** 3-5 реальних сценаріїв помилок ПЗ з побутових застосунків
**Інтерактивні елементи:** Квіз на розуміння різниці між тестуванням та debugging

---

#### **Глава 2: ОСНОВИ КОНТРОЛЮ ЯКОСТІ**

**Мета:** Розуміння концепцій QA, QC, Verification, Validation та їх взаємозв'язку

| Підрозділ | Зміст | Джерела | Ресурси |
|-----------|-------|---------|----------|
| 2.1 Якість програмного забезпечення | - ISO/IEC 25010:2011 стандарт якості<br>- 8 характеристик якості ПЗ<br>- Вимірювання якості | RWP ✓ / DATASET(QALight: osnovi/iakist-programnogo-zabezpechennia, ISO 2015) / MODERN(ISO 25010) | ![QR: ISO 25010](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/ISO/IEC_25010&margin=10) |
| 2.2 QA vs QC vs Testing | - Якість (Quality Management)<br>- Контроль якості (Operational)<br>- Тестування (One QC technique)<br>- Таблиця розрізнення | RWP ✓ / DATASET(QALight: osnovi/qa-qc-i-testuvannia, books_pdf: Didkovska 2010) / MODERN ✓ | ![QR: QA/QC/Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi/qa-qc-i-testuvannia&margin=10) |
| 2.3 Verification vs Validation | - Verification: Are we building it right?<br>- Validation: Are we building the right thing?<br>- Практичні приклади розрізнення | RWP ✓ / DATASET(QALight: osnovi/verifikatsiia-ta-validatsiia) / MODERN ✓ | ![QR: V&V Concept](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Verification_and_validation&margin=10) |
| 2.4 Концепція тестування в SDLC | - Тестування як частина розвитку<br>- Вплив моделей розробки (Waterfall, Agile)<br>- Ієрархія документів (QA Plan → Strategy → Plan → Cases) | RWP ✓ / DATASET(QA_Bible: sdlc-i-stlc) / MODERN ✓ | ![QR: SDLC Models](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://github.com/STT-VITI-22/stt-handbook/blob/main/dist/&margin=10) |
| 2.5 Ролі у тестуванні | - QA Engineer, Test Analyst, Test Automation Engineer<br>- ISTQB Career Path<br>- Вимоги та компетенції | RWP ✓ / DATASET(QALight: osnovi) / MODERN(ISTQB 4.0) | ![QR: ISTQB Roles](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.istqb.org/certification&margin=10) |

---

#### **Глава 3: ПРОЦЕСИ ТА ЦИКЛИ ТЕСТУВАННЯ**

**Мета:** Розуміння основного процесу тестування та його фаз

| Підрозділ | Зміст | Джерела | Ресурси |
|-----------|-------|---------|----------|
| 3.1 Фундаментальний процес тестування | - 6 фаз основного процесу (ISTQB)<br>- 1) Planning & Estimation<br>- 2) Analysis & Design<br>- 3) Implementation<br>- 4) Execution<br>- 5) Evaluation & Reporting<br>- 6) Closure | RWP ✓ / DATASET(QALight: osnovi/fundamentalnii-protses-testuvannia) / MODERN(ISTQB 4.0) | ![QR: Test Process](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.istqb.org/downloads&margin=10) |
| 3.2 STLC: Цикл розвитку тестування | - 7 этапов: Requirements → Design → Development → Testing → Deployment<br>- Взаємозв'язок з SDLC<br>- Артефакти на кожному етапі | RWP ✓ / DATASET(QA_Bible: sdlc-i-stlc, books_pdf: ITVDN 2024) / MODERN ✓ | ![QR: STLC Phases](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Software_testing&margin=10) |
| 3.3 Коли починати та закінчувати тестування | - Критерії входження (Entry Criteria)<br>- Критерії виходження (Exit Criteria)<br>- Кількість тестів та покриття<br>- Практичні приклади | RWP ✓ / DATASET(QALight: osnovi/koli-pochinati-ta-zakinchuvati-testuvannia) / MODERN(ISTQB 4.0) | ![QR: Entry/Exit Criteria](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi&margin=10) |
| 3.4 Матриці в тестуванні | - Requirements Traceability Matrix (RTM)<br>- Coverage Matrix<br>- Test Execution Matrix<br>- Як складати та використовувати | RWP ✓ / DATASET(QALight: osnovi/matritsia-vidpovidnosti-vimog, osnovi/matritsia-pokrittia) / MODERN ✓ | ![QR: Test Matrices](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi/matritsia-vidpovidnosti-vimog&margin=10) |
| 3.5 Практичне завдання: Manual Testing та Test Case Design  |  **Репозиторій stt-manual-testing**<br>- Створення тестових сценаріїв для реальних додатків<br>- Створити та виконати тест-кейси<br>- Позитивне та негативне тестування<br>- Документація тестових артефактів | RWP ✓ / DATASET(stt-manual-testing, practical_tasks/stt-manual-testing, QALight: osnovi) / MODERN ✓ | ![QR: stt-manual-testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://github.com/STT-VITI-22/stt-manual-testing&margin=10) |

---

#### **Глава 4: ПСИХОЛОГІЯ ТА ПРИНЦИПИ ТЕСТУВАННЯ**

**Мета:** Розуміння людського фактору та основних принципів у тестуванні

| Підрозділ | Зміст | Джерела | Ресурси |
|-----------|-------|---------|----------|
| 4.1 7 принципів тестування | - 1) Тестування показує наявність дефектів<br>- 2) Вичерпне тестування неможливе<br>- 3) Раннє тестування економить гроші<br>- 4) Кластеризація дефектів (80/20)<br>- 5) Парадокс пестициду<br>- 6) Тестування залежить від контексту<br>- 7) Відсутність помилок — це ілюзія | RWP ✓ / DATASET(QALight: osnovi/printsipi-testuvannia) / MODERN(ISTQB 4.0) | ![QR: 7 Principles](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.istqb.org/downloads&margin=10) |
| 4.2 Цілі тестування | - Знаходження дефектів<br>- Отримання інформації про якість<br>- Запобігання дефектам<br>- Побудова довіри до ПЗ | RWP ✓ / DATASET(QALight: osnovi/tsili-testuvannia) / MODERN ✓ | ![QR: Testing Goals](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi/tsili-testuvannia&margin=10) |
| 4.3 Психологія тестувальника | - Критичне мислення vs. позитивне сприйняття розробника<br>- Пошук дефектів vs. демонстрація функціональності<br>- Комунікація результатів без конфліктів<br>- Управління стресом | RWP ✓ / DATASET(QALight: osnovi/psikhologiia-testuvannia) / MODERN ✓ | ![QR: Tester Psychology](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi&margin=10) |
| 4.4 Комунікація та конфліктність | - Як звітувати про дефекти конструктивно<br>- Інтерпретація результатів<br>- Робота з розробниками та менеджерами | RWP ✓ / DATASET(QALight: osnovi) / MODERN ✓ | ![QR: Communication](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Effective_communication&margin=10) |
| 4.5 Практичні психологічні техніки | - Mind-mapping для тестування<br>- Creative testing techniques<br>- Exploratory mindset | RWP ✓ / DATASET(books_pdf: Kaner 1999, Gregory 2014) / MODERN ✓ | ![QR: Creative Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Mind_map&margin=10) |

---

### ЧАСТИНА 2: БАЗОВА ТЕОРІЯ ТЕСТУВАННЯ

Цільова аудиторія: Практикуючі тестувальники, ISTQB Foundation

---

#### **Глава 5: РІВНІ ТЕСТУВАННЯ**

**Мета:** Розуміння 4 основних рівнів тестування та їх характеристик

| Підрозділ | Зміст | Джерела | Ресурси |
|-----------|-------|---------|----------|
| 5.1 Модульне тестування (Unit Testing) | - Визначення та сфера<br>- Сфера: Функції, методи, класи<br>- Інструменти: JUnit, pytest, NUnit<br>- Білий ящик<br>- Раннє перехоплення дефектів | RWP ✓ / DATASET(QALight: rivni-testuvannia/modulne-testuvannia) / MODERN ✓ | ![QR: Unit Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Unit_testing&margin=10) |
| 5.2 Інтеграційне тестування | - Визначення та сфера<br>- Види: Big Bang, Top-Down, Bottom-Up<br>- Тестування інтеграції компонентів<br>- Інтеграційні дефекти | RWP ✓ / DATASET(QALight: rivni-testuvannia/integratsiine-testuvannia, QA_Bible: vidy-metody-urovni) / MODERN ✓ | ![QR: Integration Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Integration_testing&margin=10) |
| 5.3 Системне тестування | - Визначення та сфера<br>- Тестування цілої системи<br>- Функціональні та нефункціональні аспекти<br>- Мультиплатформне тестування | RWP ✓ / DATASET(QALight: rivni-testuvannia/sistemne-testuvannia) / MODERN ✓ | ![QR: System Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/System_testing&margin=10) |
| 5.4 Приймальне тестування (User Acceptance Testing) | - Визначення та сфера<br>- Business Acceptance Testing (BAT)<br>- UAT процес та критерії<br>- Alpha та Beta тестування<br>- User stories та acceptance criteria | RWP ✓ / DATASET(QALight: rivni-testuvannia/priimalne-testuvannia, ISTQB 4.0) / MODERN ✓ | ![QR: UAT Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Acceptance_testing&margin=10) |
| 5.5 Інші рівні тестування | - Regression testing<br>- Smoke testing<br>- Саніти-тестування<br>- Граничні тестування | RWP ✓ / DATASET(QALight, QA_Bible) / MODERN ✓ | ![QR: Testing Levels](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi&margin=10) |

**Практичні приклади:** Для кожного рівня — реальний приклад з розробки web-застосунку
**Матриця покриття:** Таблиця, яка показує кого тестує кожен рівень

---

#### **Глава 6: ТИПИ ТЕСТУВАННЯ**

**Мета:** Розуміння різних видів тестування за принципом «чорний ящик»

| Підрозділ | Зміст | Джерела | Ресурси |
|-----------|-------|---------|----------|
| 6.1 Функціональне тестування | - Базовий тип тестування<br>- Перевірка функцій аплікації<br>- Приклади: калькулятор, вхід користувача<br>- Різниця від нефункціонального | RWP ✓ / DATASET(QALight: vidi-testuvannia/funktsionalne-testuvannia) / MODERN ✓ | ![QR: Functional Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Functional_testing&margin=10) |
| 6.2 Нефункціональне тестування | - Performance Testing<br>- Security Testing<br>- Usability Testing<br>- Compliance Testing | RWP ✓ / DATASET(QALight: vidi-testuvannia/nefunktsionalne-testuvannia, QA_Bible: vidy-metody-urovni) / MODERN ✓ | ![QR: Non-Functional Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi&margin=10) |
| 6.3 Тестування продуктивності | - Performance characterization<br>- Load Testing<br>- Stress Testing<br>- Volume Testing<br>- Tools: JMeter, LoadRunner | RWP ✓ / DATASET(QALight: vidi-testuvannia/testuvannia-produktivnosti) / MODERN ✓ | ![QR: Performance Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Load_testing&margin=10) |
| 6.4 Тестування безпеки | - Security vulnerabilities<br>- Injection attacks<br>- OWASP Top 10 (Classic)<br>- Penetration testing<br>- **OWASP 2025 Updates:** Software Supply Chain Failures (#3 NEW)<br>- **Supply Chain Security Testing** 🆕<br>  - SCA tools, SBOM generation, Signed artifacts<br>  - **Real-world threat:** Shai-Hulud (2025) — npm worm | RWP ✓ / DATASET(QALight: vidi-testuvannia/testuvannia-bezpeki, TRENDS_2024_2025_RESEARCH.md) / MODERN (OWASP 2025) ✓ | ![QR: Security Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://owasp.org/Top10&margin=10) |
| 6.5 Тестування юзабіліті та інші типи | - Usability Testing<br>- Compatibility Testing<br>- Configuration Testing<br>- Localization & Internationalization Testing<br>- Disaster Recovery & Business Continuity Testing | RWP ✓ / DATASET(QALight: vidi-testuvannia/) / MODERN ✓ | ![QR: Usability Testing](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Usability_testing&margin=10) |

---

#### **Глава 7: ТЕХНІКИ ТЕСТУВАННЯ ТА ДИЗАЙН**

**Мета:** Розуміння методів розроблення тест-кейсів та проектування тестів

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 7.1 Білий ящик тестування | - Static Analysis<br>- **Керуючий граф програми (Control Flow Graph - CFG)**<br>  - Графічне представлення потоку управління<br>  - Вузли та ребра, базові блоки коду<br>  - Характеристики CFG та застосування<br>- Code Coverage (C0, C1, C2, ..., C∞)<br>  - C0: Statement Coverage (всі оператори)<br>  - C1: Branch Coverage (всі розгалуження)<br>  - C2: Path Coverage (всі шляхи)<br>  - Більш високі рівні покриття<br>- **Цикломатична складність (McCabe Complexity)**<br>  - Вимір складності коду на основі CFG<br>  - Формула: M = E − N + 2P<br>  - Застосування при розробці та тестуванні<br>  - Рекомендовані межі складності (≤10)<br>- Statement Coverage<br>- Branch Coverage<br>- Path Coverage | RWP ✓ / DATASET(QALight: tipi-testuvannia/white-black-grey-box, QA_Bible: test-dizain/static-static-analysis, books_pdf: Copeland 2004, Avramenko 2017, Didkovska 2011) / MODERN ✓ |
| 7.2 Чорний ящик тестування | - Functional specification focus<br>- No code knowledge<br>- Techniques (BVA, ECP, DTT)<br>- Test case design from requirements | RWP ✓ / DATASET(QALight: tipi-testuvannia/white-black-grey-box, books_pdf: Beizer 2004) / MODERN ✓ |
| 7.3 Еквівалентне розподілення (Equivalence Partitioning) | - Теорія та принципи<br>- Практичні приклади<br>- Дійсні та невірні партиції<br>- Таблиця еквівалентного розподілення | RWP ✓ / DATASET(QA_Bible: test-dizain, books_pdf: Copeland 2004) / MODERN ✓ |
| 7.4 Аналіз граничних значень (Boundary Value Analysis) | - BVA Теорія<br>- Edge cases та corner cases<br>- Off-by-one errors<br>- Практичні приклади | RWP ✓ / DATASET(QA_Bible: test-dizain, books_pdf: Copeland 2004, Kulikov 2020) / MODERN ✓ |
| 7.5 Таблиці рішень (Decision Tables) | - Decision table structure<br>- Logical combinations<br>- Умови та дії<br>- Спрощення та мінімізація тестів | RWP ✓ / DATASET(QA_Bible: test-dizain, books_pdf: Copeland 2004) / MODERN ✓ |
| 7.6 Тестування переходів стану (State Transition Testing) | - State diagrams<br>- Transitions та events<br>- Valid та invalid transitions<br>- Практичні приклади (UI workflows) | RWP ✓ / DATASET(QA_Bible: test-dizain) / MODERN ✓ |
| 7.7 Використання кейсів для тестування | - User Story vs. Use Case<br>- Test cases from use cases<br>- Happy path vs. exception paths | RWP ✓ / DATASET(QALight: osnovi, ISTQB 4.0) / MODERN ✓ |
| **7.8 Практичне завдання: Unit тестування з Mocha/Chai** 🆕 | - **Проект stt-pz-1 (GitHub)**<br>- Налаштування браузерного тестового середовища<br>- BDD/TDD підходи в Mocha<br>- Assertion бібліотека Chai<br>- Test case для реальних функцій<br>- Browser-based test execution<br>- **Recursos:** https://github.com/STT-VITI-22/stt-pz-1 | RWP ✓ / DATASET(stt-pz-1, practical_tasks/stt-pz-1-mocha-chai, QALight: osnovi) / MODERN ✓ |

**Порівняльна таблиця:** Коли використовувати кожну техніку

**Практичні завдання:** Розділ 7 має практичне завдання для закріплення знань про техніки дизайну тестів

---

#### **Глава 8: УПРАВЛІННЯ ДЕФЕКТАМИ**

**Мета:** Розуміння жизненного цикла дефектів та управління якістю

| Підрозділ | Зміст | Джерела | Ресурси |
|-----------|-------|---------|----------|
| 8.1 Терміни: Error, Defect, Failure, Bug | - Точні визначення ISTQB<br>- Причина → Дефект → Вплив<br>- Практичні приклади з ланцюжком<br>- Синоніми та вживання | RWP ✓ / DATASET(QALight: osnovi, defekt, books_pdf) / MODERN(ISTQB 4.0) | ![QR: Error vs Defect](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.istqb.org&margin=10) |
| 8.2 Класифікація дефектів | - За серйозністю: Critical, Major, Minor, Trivial<br>- За пріоритетом: High, Medium, Low<br>- За типом (Functional, Logic, UI, API)<br>- За впливом на користувача | RWP ✓ / DATASET(QALight: defekt/klasifikatsiia-defektiv) / MODERN ✓ | ![QR: Defect Classification](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi&margin=10) |
| 8.3 Життєвий цикл дефекта | - Статуси: New → Open → Assigned → In Progress → Fixed → Verified → Closed<br>- Повторне відкриття дефектів<br>- Деференція та відкладення | RWP ✓ / DATASET(QALight: defekt/zhittievii-tsikl-defektiv, QA_Bible: obshee) / MODERN ✓ | ![QR: Defect Lifecycle](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/osnovi&margin=10) |
| 8.4 Bug Report (Звіт про дефект) | - Структура звіту<br>- Обов'язкові поля (ID, Title, Description, Steps)<br>- Скріншоти та логи<br>- Приклади хороших та поганих звітів | RWP ✓ / DATASET(QALight: testovi-artefakti/bug-report-zvit-pro-pomilku) / MODERN ✓ | ![QR: Bug Report Template](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://qalight.ua/testovi-artefakti&margin=10) |
| 8.5 Вартість дефектів | - Економіка знаходження дефектів рано<br>- Витрати на виправлення на різних етапах<br>- ROI тестування | RWP ✓ / DATASET(QALight: osnovi/skilki-koshtuiut-defekti, books_pdf: Gregory 2014) / MODERN ✓ | ![QR: Defect Cost](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://en.wikipedia.org/wiki/Software_defect&margin=10) |
| 8.6 Інструменти управління дефектами | - JIRA (основний)<br>- Bugzilla, Azure DevOps, YouTrack<br>- Trello (канбан-стиль)<br>- Worksection (управління проєктами) | RWP ✓ / DATASET(QA_Bible: obshee) / MODERN ✓ | ![QR: Defect Tools](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.atlassian.com/software/jira&margin=10) |
| **8.7 Практичне завдання: Bug Report та Defect Management** 🆕 | - **Проект stt-bug-reporting**<br>- Структура Bug Report та класифікація<br>- Bug Report у JIRA<br>- Життєвий цикл дефекта<br>- Root Cause Analysis (RCA) | RWP ✓ / DATASET(stt-bug-reporting, practical_tasks/stt-bug-reporting, QALight: defekt) / MODERN ✓ | ![QR: stt-bug-reporting](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://github.com/STT-VITI-22/stt-bug-reporting&margin=10) |

---

### ЧАСТИНА 3: РОЗШИРЕНІ ТЕМИ

Цільова аудиторія: ISTQB Advanced, Test Managers, Lead Engineers

---

#### **Глава 9: ТЕСТУВАННЯ У AGILE/DEVOPS СЕРЕДОВИЩАХ**

**Мета:** Розуміння тестування в сучасних гнучких методологіях розробки

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 9.1 Основи Agile та Scrum | - Agile Manifesto та Principles<br>- Scrum Framework (Roles, Artifacts, Ceremonies)<br>- Sprint Planning та Execution<br>- Definition of Done | RWP ✓ / DATASET(QALight: osnovi/agile.md, QA_Bible: sdlc-i-stlc/agile, books_pdf: Gregory 2014, Schwaber 2020) / MODERN(ISTQB 4.0) |
| 9.2 LEAN методологія | - 5 принципів LEAN<br>- Мuda, Mura, Muri концепції<br>- Kanban система та WIP Limit<br>- Continuous improvement (Kaizen) | RWP ✓ / DATASET(TERMINOLOGY.md, QALight: osnovi/agile.md, QA_Bible: sdlc-i-stlc) / MODERN ✓ |
| 9.3 Тестування в Agile спринтах | - Тестування в спринті<br>- Acceptance testing та user stories<br>- Test automation для Agile<br>- Collaboration between QA and Developers | RWP ✓ / DATASET(QALight: osnovi/agile, QA_Bible: sdlc-i-stlc, books_pdf: Gregory 2014) / MODERN(ISTQB 4.0) |
| 9.4 Continuous Integration & Continuous Deployment | - CI/CD Pipeline<br>- Automated testing у CI<br>- Test automation strategy для CD<br>- Quality gates та release cycles | RWP ✓ / DATASET(QALight: zagalne/shcho-take-ci-continuous-integration, QA_Bible: sdlc-i-stlc) / MODERN ✓ |
| 9.5 DevOps та тестування | - DevOps culture та collaboration<br>- Операційне тестування<br>- Production monitoring та defect detection<br>- Shift-left та shift-right testing | RWP ✓ / DATASET(books_pdf: SoftwareTestingHouse 2023, ITVDN 2024) / MODERN ✓ |
| 9.6 BDD та TDD підходи | - Test-Driven Development (TDD)<br>- Behavior-Driven Development (BDD)<br>- Gherkin syntax (Given-When-Then)<br>- Tools: Cucumber, SpecFlow | RWP ✓ / DATASET(QA_Bible: sdlc-i-stlc) / MODERN ✓ |
| **9.7 Практичні завдання: TDD та BDD у Agile** 🆕 | - **Проект stt-pz-2: TDD з Jest** (>90% покриття)<br>- **Проект stt-pz-4: BDD з Jest та spyOn mocking**<br>- Red-Green-Refactor цикл<br>- BDD Given-When-Then структура<br>- Mocking та спеціалізовані техніки<br>- Integration з CI/CD pipeline<br>- **Ресурси:** https://github.com/STT-VITI-22/stt-pz-2, https://github.com/STT-VITI-22/stt-pz-4 | RWP ✓ / DATASET(stt-pz-2, stt-pz-4, practical_tasks/stt-pz-2-jest-tdd, practical_tasks/stt-pz-4-jest-bdd) / MODERN ✓ |

---

#### **Глава 10: УПРАВЛІННЯ ТЕСТУВАННЯМ І ПЛАНУВАННЯ**

**Мета:** Розуміння управління тестовим процесом на організаційному рівні

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 10.1 Тестова стратегія | - Визначення тестової стратегії<br>- Рівні тестування за стратегією<br>- Типи тестування та розподіл ресурсів<br>- Вибір інструментів | RWP ✓ / DATASET(QALight: testovi-artefakti/testova-strategiia) / MODERN(ISTQB 4.0) |
| 10.2 Тестовий план | - Структура тестового плану<br>- Обсяг та цілі<br>- Ресурси та розклад<br>- Ризики та рекомендації | RWP ✓ / DATASET(QALight: testovi-artefakti/test-plan) / MODERN ✓ |
| 10.3 Оцінка та планування тестування | - Estimation techniques<br>- Effort estimation<br>- Risk-based testing<br>- Resource allocation | RWP ✓ / DATASET(QA_Bible: obshee) / MODERN ✓ |
| 10.4 Тестова документація | - Test case specifications<br>- Test procedures<br>- Test summary reports<br>- Dokumentation standards | RWP ✓ / DATASET(QALight: testovi-artefakti/) / MODERN ✓ |
| 10.5 Метрики тестування | - Test coverage metrics<br>- Defect metrics<br>- Test execution metrics<br>- Quality metrics | RWP ✓ / DATASET(QA_Bible: obshee, books_pdf: Hrytsiuk 2018) / MODERN ✓ |
| 10.6 Управління ризиками в тестуванні | - Risk identification та analysis<br>- Risk-based testing approach<br>- Пріоритизація тестів<br>- Mitigation strategies | RWP ✓ / DATASET(QA_Bible: obshee, books_pdf: Gregory 2014) / MODERN ✓ |

---

#### **Глава 11: ТЕХНІЧНІ ОСНОВИ ДЛЯ ТЕСТУВАЛЬНИКІВ**

**Мета:** Розуміння технічних концепцій, необхідних для сучасного тестування

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 11.1 Основи веб-технологій | - HTML, CSS базиці<br>- JavaScript основи<br>- HTTP/HTTPS protocol<br>- Web browsers та rendering | RWP ✓ / DATASET(QALight: osnovi/html-ta-css-dlia-testuvalnikiv, zagalne/) / MODERN ✓ |
| 11.2 API та веб-сервіси | - REST API basics<br>- HTTP методи (GET, POST, PUT, DELETE)<br>- JSON та XML формати<br>- API testing tools (Postman, Insomnia) | RWP ✓ / DATASET(QALight: zagalne/shcho-take-api, zagalne/shcho-take-json, zagalne/protses-komunikatsii-pri-vikoristanni-api) / MODERN ✓ |
| 11.3 Мережі та протоколи | - IP адреси та DNS<br>- TCP/IP, UDP<br>- HTTP, HTTPS, FTP<br>- Cookies та Sessions | RWP ✓ / DATASET(QALight: protokoli/) / MODERN ✓ |
| 11.4 Бази даних для тестувальників | - SQL базиці<br>- SELECT, WHERE, JOIN statements<br>- Database verification in tests<br>- Tools: DBeaver, MySQL Workbench | RWP ✓ / DATASET(QALight: bazi-danikh-v-testuvanni/) / MODERN ✓ |
| 11.5 Git та версійне контролю | - Git basics (clone, pull, push)<br>- Branches та commits<br>- Pull requests<br>- Collaboration in development | RWP ✓ / DATASET(QALight: zagalne/shcho-take-git) / MODERN ✓ |
| 11.6 Архітектура ПЗ для тестування | - Monolithic vs. Microservices<br>- Client-Server architecture<br>- APIs, interfaces<br>- Deployment models | RWP ✓ / DATASET(QALight: zagalne/monolitna-arkhitektura, zagalne/mikroservisna-arkhitektura) / MODERN ✓ |
| **11.7 Практичне завдання: API тестування та Mock дані** 🆕 | - **Проект stt-pz-3: Jest API тестування**<br>- Mock функції та Jest.mock()<br>- Ice and Fire API приклади<br>- JSON валідація та структури<br>- Handling асинхронних операцій<br>- Mock data management та fixtures<br>- **Ресурс:** https://github.com/STT-VITI-22/stt-pz-3 | RWP ✓ / DATASET(stt-pz-3, practical_tasks/stt-pz-3-jest-api, QALight: zagalne/shcho-take-api) / MODERN ✓ |

---

#### **Глава 12: МЕТРИКИ ТА ОЦІНЮВАННЯ ЯКОСТІ**

**Мета:** Розуміння як вимірювати та оцінювати якість ПЗ

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 12.1 ISO/IEC 25010:2011 стандарт якості | - 8 характеристик якості<br>- Функціональна відповідність<br>- Надійність<br>- Продуктивність<br>- Вживаність та ін. | RWP ✓ / DATASET(QALight: osnovi/iakist-programnogo-zabezpechennia-za-iso-iec-25010-2011) / MODERN(ISO 25010) |
| 12.2 Метрики покриття тестування | - Code Coverage Levels (C0 до C∞):<br>  - **C0: Statement Coverage** — покриття всіх операторів коду<br>  - **C1: Branch Coverage** — покриття всіх розгалужень (if/else)<br>  - **C2: Path Coverage** — покриття всіх можливих шляхів<br>  - Вищі рівні (C∞) — покриття всіх циклічних комбінацій<br>- **Керуючий граф програми (CFG)** та метрики на його основі:<br>  - Графічне представлення потоку контролю<br>  - Незалежні шляхи в графі<br>  - Застосування для розрахунку кількості необхідних тестів<br>- **Цикломатична складність (Cyclomatic Complexity)**<br>  - Метрика складності на основі CFG<br>  - Визначає мінімальну кількість тестів для покриття шляхів<br>  - Формула: M = E − N + 2P (Е = ребра, N = вузли, P = компоненти)<br>- Requirement coverage %<br>- Test case execution rate<br>- Defect detection effectiveness | RWP ✓ / DATASET(QA_Bible: obshee, test-dizain/static-static-analysis, books_pdf: Hrytsiuk 2018, Copeland 2004, Avramenko 2017) / MODERN ✓ |
| 12.3 Метрики дефектів | - Defect density (dpu)<br>- Defect distribution<br>- Defect escape rate<br>- Mean time between failures (MTBF) | RWP ✓ / DATASET(books_pdf: Hrytsiuk 2018, Katayeva 2020) / MODERN ✓ |
| 12.4 Метрики процесу тестування | - Test execution time<br>- Effort spent on testing<br>- Cost per test case<br>- Schedule performance | RWP ✓ / DATASET(QA_Bible: obshee) / MODERN ✓ |
| 12.5 Звітування про якість | - Quality reports for management<br>- Trend analysis<br>- Risk assessment report<br>- Recommendations | RWP ✓ / DATASET(books_pdf) / MODERN ✓ |
| **12.6 Synthetic Monitoring & Observability** 🆕 | - **Synthetic Monitoring + Real User Monitoring (RUM)**<br>- Continuous quality checks з искусственных сценариев<br>- User Experience Observation (UXO) концепція<br>- OpenTelemetry integration для distributed tracing<br>- Grafana k6 для synthetic load tests<br>- Datadog, New Relic, Uptrace integrazioni<br>- Alerting та Quality Gates у production<br>- **Adoption growth:** 30% (2024) → 65% (2025) → 85% (2026) | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN (2024-2026) ✓ |
| **12.7 Практичне завдання: ELK + MCP AI Log Analysis** 🆕 | - **Проект stt-elk-mcp-logging**<br>- Elasticsearch, Logstash, Kibana (ELK) стек<br>- Структуроване логування з Python/Node.js<br>- Logstash pipelines для парсингу та збагачення<br>- Kibana dashboards для моніторингу<br>- **MCP сервер для AI аналізу** (NEW)<br>- Claude AI integration для аномалій та RCA<br>- Anomaly detection та alerting<br>- Docker Compose full stack<br>- **Ресурс:** https://github.com/STT-VITI-22/stt-elk-mcp-logging | RWP ✓ / DATASET(stt-elk-mcp-logging, practical_tasks/stt-elk-mcp-logging, books_pdf) / MODERN ✓ |

---

### ЧАСТИНА 4: СУЧАСНА ПРАКТИКА ТА ШІ

Цільова аудиторія: ISTQB Advanced, Specialists, Senior Engineers

---

#### **Глава 13: АВТОМАТИЗАЦІЯ ТЕСТУВАННЯ**

**Мета:** Розуміння інструментів та техник автоматизованого тестування

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 13.1 Основи автоматизації | - Коли автоматизувати<br>- Переваги та недоліки<br>- Інвестиції та ROI<br>- Стратегія автоматизації | RWP ✓ / DATASET(QALight: avtomatizatsiia/avtomatizovane-testuvannia) / MODERN ✓ |
| 13.2 Вибір інструментів автоматизації | - Web automation: Selenium, Cypress, Playwright<br>- API automation: REST Assured, Postman<br>- Mobile automation: Appium<br>- Вибір за критеріями | RWP ✓ / DATASET(QALight: avtomatizatsiia/iak-obrati-instrument-avtomatizatsii) / MODERN ✓ |
| 13.3 Локатори та селектори | - XPath (абсолютний та відносний)<br>- CSS Selectors<br>- ID, Name, Class, Tag селектори<br>- Best practices | RWP ✓ / DATASET(QALight: avtomatizatsiia/x-path-lokatori-teoriia, avtomatizatsiia/iak-napisati-x-path-lokator, avtomatizatsiia/vikoristannia-tagname) / MODERN ✓ |
| 13.4 Page Object Model | - Design pattern для тестів<br>- Організація коду<br>- Повторне використання та обслуговування<br>- Best practices | RWP ✓ / DATASET(QA_Bible: avtomatizaciya-testirovaniya) / MODERN ✓ |
| 13.5 CI/CD інтеграція | - Jenkins pipeline<br>- GitHub Actions<br>- GitLab CI<br>- Test execution в pipeline | RWP ✓ / DATASET(QALight: zagalne/shcho-take-ci-continuous-integration, QA_Bible: avtomatizaciya-testirovaniya) / MODERN ✓ |
| 13.6 API automation | - REST API testing<br>- Request-Response cycle<br>- JSON schema validation<br>- Mock servers | RWP ✓ / DATASET(QA_Bible: avtomatizaciya-testirovaniya) / MODERN ✓ |
| **13.7 Cloud-Native & Kubernetes Testing** 🆕 | - **Kubernetes adoption 96%, але готовність тестування тільки 34%**<br>- Testkube framework для K8s tестування<br>- Container image scanning та security<br>- K8s manifest validation та policy testing<br>- Network policies та service mesh тестування<br>- Helm charts verification<br>- CRD (Custom Resource Definition) тестування<br>- GitOps integration (ArgoCD, Flux)<br>- Tools: Testkube, Kubetest, Kyverno<br>- **Adoption gap:** 96% use K8s (2024), 82% deploy AI models, but only 34% adapted testing | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN (2024-2026) ✓ |
| **13.8 Практичне завдання: Modern Test Automation з Cypress** 🆕 | - **Проект stt-pz-5: End-to-End тестування**<br>- Cypress порівняно з Selenium/Playwright<br>- Real user interactions та workflows<br>- Element selection та assertions<br>- E2E test organization і patterns<br>- Real-world calculator testing<br>- **Ресурс:** https://github.com/STT-VITI-22/stt-pz-5 | RWP ✓ / DATASET(stt-pz-5, practical_tasks/stt-pz-5-cypress-e2e) / MODERN ✓ |

---

#### **Глава 14: МОБІЛЬНЕ ТЕСТУВАННЯ**

**Мета:** Розуміння особливостей тестування мобільних додатків

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 14.1 Особливості мобільного тестування | - Різноманіття пристроїв та ОС<br>- Network conditions<br>- Battery та memory constraints<br>- Screen size variations | RWP ✓ / DATASET(QALight: android/, defekt/testuvannia-mobilnikh-dodatkiv, QA_Bible: mobilnoe-testirovanie) / MODERN ✓ |
| 14.2 iOS тестування | - iPhone/iPad devices<br>- XCUITest framework<br>- TestFlight for beta testing<br>- Specifics та вызовы | RWP ✓ / DATASET(QA_Bible: mobilnoe-testirovanie) / MODERN ✓ |
| 14.3 Android тестування | - Android devices та emulator<br>- Appium framework<br>- Android Studio testing tools<br>- Native apps vs. Web apps | RWP ✓ / DATASET(QALight: android/, QA_Bible: mobilnoe-testirovanie) / MODERN ✓ |
| 14.4 Мобільні на відміну від веб-додатків | - Architectural differences<br>- User experience expectations<br>- Performance considerations<br>- Security aspects | RWP ✓ / DATASET(QALight: osnovi/mobilnii-ta-veb-dodatok-u-chomu-riznitsia) / MODERN ✓ |
| 14.5 Тестування у різних мережевих умовах | - 3G, 4G, 5G, WiFi<br>- Offline functionality<br>- Network switching scenarios<br>- Bandwidth limitations | RWP ✓ / DATASET(QA_Bible: mobilnoe-testirovanie) / MODERN ✓ |

---

#### **Глава 15: ТЕСТУВАННЯ У РІЗНИХ СФЕРАХ**

**Мета:** Розуміння специфіки тестування в різних галузях

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 15.1 Фінансова та банківська сфера | - Security вимоги (PCI DSS)<br>- Regulatory compliance<br>- Транзакційна цілісність<br>- High-volume processing | RWP ✓ / DATASET(QA_Bible: testirovanie-v-raznykh-sferakh-oblastyakh) / MODERN ✓ |
| 15.2 Медицина та healthcare | - FDA regulations<br>- HIPAA compliance<br>- Safety-critical systems<br>- Data privacy | RWP ✓ / DATASET(QA_Bible: testirovanie-v-raznykh-sferakh-oblastyakh) / MODERN ✓ |
| 15.3 Телекомунікаційні системи | - Масштабування та надійність<br>- Інтерфейс з третіми сторонами<br>- Глобальна покривність<br>- Специфічні стандарти | RWP ✓ / DATASET(QA_Bible: testirovanie-v-raznykh-sferakh-oblastyakh) / MODERN ✓ |
| 15.4 ІоТ та вбудовані системи | - Hardware integration<br>- Real-time constraints<br>- Firmware testing<br>- Specifics та challenges | RWP ✓ / DATASET(QA_Bible: testirovanie-v-raznykh-sferakh-oblastyakh) / MODERN ✓ |
| 15.5 E-commerce та веб-сервіси | - Performance under load<br>- Payment processing<br>- User experience<br>- Security considerations | RWP ✓ / DATASET(QALight: osnovi/testuvannia-veb-proiektiv-osnovni-etapi-ta-poradi, QA_Bible) / MODERN ✓ |
| 15.6 Інші сфери та специфіка | - Game development<br>- VR/AR applications<br>- AI/ML systems<br>- Cloud-based services | RWP ✓ / DATASET(QA_Bible: ai-v-testirovanii, testirovanie-v-raznykh-sferakh) / MODERN ✓ |

---

#### **Глава 15 (Альтернативна): ТЕСТУВАННЯ В ЕРУ ШІ ТА LLM МОДЕЛЕЙ** 🆕

**Мета:** Розуміння роботи з AI-моделями при тестуванні та нових підходів до автоматизації

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 15.1 AI for Testing | - Генерація тест-дизайну через промпти<br>- Автоматичне оновлення локаторів (Self-healing)<br>- QA-агенти та Agentic Development | DATASET(QA_Bible: ai-v-testirovanii/15 файлів) / MODERN ✓ |
| 15.2 Testing AI Systems | - Недетермінованість нейромереж<br>- Проблема тестового оракула<br>- Оцінка точності моделей (Confusion Matrix)<br>- Вимірювання якості AI продукту | DATASET(QA_Bible: ai-v-testirovanii) / MODERN ✓ |
| 15.3 Верифікація LLM | - Метаморфне тестування (Metamorphic Testing)<br>- Оцінка галюцинацій та Red Teaming<br>- Стійкість до джейлбрейків та атак<br>- Prompt injection тестування | DATASET(QA_Bible: ai-v-testirovanii) / MODERN ✓ |
| **15.4 Agentic AI Testing** 🆕 | - **Автономні AI агенти для тестування**<br>- Generative test case creation<br>- **Self-healing mechanisms** (88% reduction в maintenance)<br>- Production failure → test conversion<br>- Autonomous test execution & diagnostics<br>- Tools: CloudQA, TestGrid, Tricentis AI Suite<br>- **Adoption trajectory:** 5% (2024) → 30% (2025) → 70% (2026) | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN (2024-2026) ✓ |
| 15.5 Human-in-the-Loop (HITL) | - Interactive testing з ШІ<br>- Feedback loop для моделей<br>- Continuous learning систем<br>- Quality gates для AI моделей | DATASET(QA_Bible: human-in-the-loop-hitl.md) / MODERN ✓ |

---

#### **Глава 16: КАР'ЄРА ТА СЕРТИФІКАЦІЯ**

**Мета:** Розуміння кар'єрного шляху у тестуванні та професійного розвитку

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 16.1 ISTQB сертифікація | - ISTQB Foundation Level<br>- ISTQB Advanced (Test Analyst, Test Manager)<br>- ISTQB Specialist (Security, Performance, AI)<br>- Нові сертифікації: CT-AI, CT-GenAI | RWP ✓ / DATASET(QALight: osnovi/shcho-novogo-v-istqb-foundation-level-syllabus-v-4-0) / MODERN(ISTQB 4.0) |
| 16.2 Кар'єрні шляхи в QA | - Junior QA Engineer<br>- QA Engineer (Manual & Automation)<br>- Senior QA / Lead QA<br>- QA Manager / QA Director<br>- Спеціалізація (Security QA, Performance, AI QA) | RWP ✓ / DATASET(QALight: osnovi, QA_Bible: faq-dlya-novichkov) / MODERN ✓ |
| 16.3 Професійні навички | - Technical skills (Automation, API, DB, Linux)<br>- Soft skills (Communication, Problem-solving)<br>- Domain knowledge<br>- Continuous learning | RWP ✓ / DATASET(QA_Bible: faq-dlya-novichkov) / MODERN ✓ |
| 16.4 Практичні поради для новачків | - Як почати у QA<br>- Перші проекти та помилки<br>- Побудова портфоліо<br>- Спільнота та ресурси | RWP ✓ / DATASET(QALight: osnovi, QA_Bible: faq-dlya-novichkov) / MODERN ✓ |
| 16.5 Технологічні тренди та майбутнє | - AI-augmented testing<br>- DevOps та автоматизація<br>- Embedded та IoT тестування<br>- Вибір спеціалізації | RWP ✓ / DATASET(QA_Bible: ai-v-testirovanii) / MODERN ✓ |

---

### ЧАСТИНА 5: EMBEDDED QA, IoT ТА DefTech 🆕

Цільова аудиторія: Embedded Engineers, IoT testers, Hardware QA, Military/Defence specialists

---

#### **Глава 17: ОСНОВИ СХЕМОТЕХНІКИ ТА МІКРОКОНТРОЛЕРІВ ДЛЯ QA** 🆕

**Мета:** Розуміння базових концепцій апаратури для тестування вбудованих систем

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 17.1 Читання архітектурних схем | - Компоненти та їх символи<br>- Технічні специфікації (Datasheet)<br>- Взаємозв'язки сигналів<br>- Робота з документацією виробника | DATASET(QA_Bible: телекомунікаційний домен) / MODERN ✓ |
| 17.2 GPIO та цифрові входи/виходи | - General Purpose I/O порти<br>- Рівні сигналу (HIGH/LOW)<br>- Pull-up та pull-down резистори<br>- Режими I/O (input, output, PWM) | DATASET(LIMITED) / MODERN ✓ |
| 17.3 Апаратні переривання (ISR) | - Interrupt Service Routine принципи<br>- Приорітизація переривань<br>- Дебаунсинг та фільтрація сигналів<br>- Синхронізація та Race Conditions | DATASET(LIMITED) / MODERN ✓ |
| 17.4 Button Bouncing та Debounce | - Фізичне явище контакту<br>- Hardware debounce-фільтри<br>- Software debounce-алгоритми<br>- Тестування у системах miltech | DATASET(LIMITED) / MODERN ✓ |

**Статус джерел:** ⚠️ 30% покрито

---

#### **Глава 18: ПРОТОКОЛЬНИЙ АНАЛІЗ ТА РОБОТА З ОБЛАДНАННЯМ** 🆕

**Мета:** Розуміння низькорівневої комунікації та діагностики апаратури

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 18.1 Низькорівневі протоколи передачі | - UART (Serial Communication)<br>- I²C (Inter-Integrated Circuit)<br>- SPI (Serial Peripheral Interface)<br>- Порівняння та вибір протоколу | DATASET(LIMITED) / MODERN ✓ |
| 18.2 Апаратні та віртуальні інструменти | - Логічні аналізатори (PulseView/Sigrok)<br>- Осцилографи та вимірювання<br>- Мультиметри та діагностика<br>- Програмний монітор послідовного портфеля (Serial Monitor) | DATASET(LIMITED) / MODERN ✓ |
| 18.3 Аналіз логів та діагностика | - Логи перезавантаження мікроконтролера<br>- Фіксація патернів «падіння» плати<br>- JTAG та дебаггери<br>- Post-mortem аналіз крешів | DATASET(LIMITED) / MODERN ✓ |

**Статус джерел:** ⚠️ 20% покрито

---

#### **Глава 19: НЕФУНКЦІОНАЛЬНІ СЦЕНАРІЇ «ЗАЛІЗА» ТА НАДІЙНІСТЬ** 🆕

**Мета:** Розуміння нефункціональних вимог у вбудованих системах

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 19.1 Watchdog Timer та захист від зависань | - Концепція WDT та переповнення<br>- Резет-механізми<br>- Тестування захисту від нескінченних циклів<br>- Таймаути і затримки | DATASET(LIMITED) / MODERN ✓ |
| 19.2 Енергозбереження та режими сну | - Normal Mode vs Deep Sleep<br>- Wake-up механізми<br>- Споживання електроенергії при тестуванні<br>- Батарейні системи | DATASET(LIMITED) / MODERN ✓ |
| 19.3 Аварійні умови та надійність | - Brown-out (падіння напруги)<br>- Міттєве знеструмлення та відновлення<br>- Дані в EEPROM/RTC при крахі<br>- Fault injection тестування | DATASET(LIMITED) / MODERN ✓ |
| 19.4 ESD та EMI стійкість | - Електростатичний розряд<br>- Електромагнітні завади<br>- Тестування у стресових умовах<br>- Стандарти та сертифікація (IEC, FCC) | DATASET(LIMITED) / MODERN ✓ |

**Статус джерел:** ⚠️ 25% покрито

---

#### **Глава 20: АВТОМАТИЗАЦІЯ ТЕСТУВАННЯ ПРОШИВОК (FIRMWARE AUTOMATION)** 🆕

**Мета:** Розуміння побудови фреймворків для тестування вбудованого ПО

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 20.1 Специфіка Firmware Automation | - На базі Python та Pytest<br>- Відмінності від web automation<br>- Hardware integration challenges<br>- CI/CD для embedded систем | DATASET(LIMITED) / MODERN ✓ |
| 20.2 Робота з послідовним портом | - Бібліотека pyserial<br>- UART комунікація та CLI пристрою<br>- Парсинг відповідей мікроконтролера<br>- Асинхронна обробка даних | DATASET(LIMITED) / MODERN ✓ |
| 20.3 Граничне тестування CLI-команд | - Boundary Value Testing для вводу<br>- Переповнення буфера мікроконтролера<br>- Обробка помилок та исключень<br>- Fuzzing та поломані команди | DATASET(LIMITED) / MODERN ✓ |
| 20.4 Mock та емуляція обладнання | - Hardware mocking у тестах<br>- Віртуальний COM port<br>- Симуляція сенсорів та датчиків<br>- In-the-loop тестування (SIL, HIL) | DATASET(LIMITED) / MODERN ✓ |

**Статус джерел:** ⚠️ 35% покрито

---

#### **Глава 21: МЕРЕЖЕВИЙ IoT-РІВЕНЬ, CONNECTIVITY ТА ПОЛЬОВІ УМОВИ** 🆕

**Мета:** Розуміння мережевого рівня та комунікації IoT пристроїв

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 21.1 RTOS та Embedded Linux | - Real-Time Operating Systems (FreeRTOS, RTOS)<br>- Embedded Linux (Yocto, Buildroot)<br>- Linux kernel за ШІ для embedded<br>- Процесні моделі та scheduling | DATASET(LIMITED) / MODERN ✓ |
| 21.2 Wi-Fi/MQTT та комунікація | - MQTT протокол та publish-subscribe<br>- Wi-Fi підключення та дисконекти<br>- Автоматичне переконнектування<br>- Кешування даних на пристрої | DATASET(LIMITED) / MODERN ✓ |
| 21.3 Тестування сумісності та взаємодії | - Interoperability з різними маршрутизаторами<br>- Мережевий обладнання (коммутатори, точки доступу)<br>- Версійна сумісність протоколів<br>- Cross-platform тестування | DATASET(LIMITED) / MODERN ✓ |
| 21.4 DefTech та польові умови | - Базові навички паяння та ремонту<br>- Експлуатація у складних умовах<br>- Вологість, температура, вібрація<br>- Військові та критичні системи | DATASET(LIMITED) / MODERN ✓ |

**Статус джерел:** ⚠️ 30% покрито

---

#### **Глава 22: МЕТОДОЛОГІЯ ROOT CAUSE ANALYSIS (RCA) ТА ЗВІТИ ДЛЯ ЗАЛІЗА** 🆕

**Мета:** Розуміння аналізу першопричин та документування у Embedded QA

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 22.1 Root Cause Analysis (RCA) | - Поняття та застосування RCA<br>- Локалізація багів: «код чи залізо»<br>- 5 Why техніка<br>- Fishbone (Ishikawa) діаграми | DATASET(LIMITED) / MODERN ✓ |
| 22.2 Hardware Validation Report | - Шаблон звіту для апаратури<br>- Умови тестування та конфігурація<br>- Результати та висновки<br>- Рекомендації та follow-up | DATASET(LIMITED) / MODERN ✓ |
| 22.3 Master Test Plan для Embedded | - Структура плану для заліза<br>- Risk Matrix та пріоритизація<br>- Ресурси та часовий графік<br>- Exit Criteria для embedded | DATASET(LIMITED) / MODERN ✓ |
| 22.4 Документація та трейсбілити | - Requirements Traceability для hardware<br>- Test Case стандартизація<br>- Revision control для документації<br>- Архівування та історія версій | DATASET(LIMITED) / MODERN ✓ |

**Статус джерел:** ⚠️ 25% покрито

---

#### **Глава 23: CHAOS ENGINEERING & RESILIENCE TESTING** 🆕

**Мета:** Розуміння тестування стійкості системи через контрольоване впровадження відмов

| Підрозділ | Зміст | Джерела |
|-----------|-------|---------|
| 23.1 Основи Chaos Engineering | - Поняття та філософія Chaos Engineering<br>- Steady-state hypothesis<br>- Fault injection testing (FIT)<br>- Controlled chaos vs catastrophic failures<br>- **Adoption growth:** 15% (2024) → 40% (2025) → 65% (2026) | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN (2024-2026) ✓ |
| 23.2 Chaos Engineering Tools & Platforms | - **Harness** — chaos-as-a-service platform<br>- **Gremlin** — production chaos engineering<br>- **LitmusChaos** — Kubernetes-native chaos<br>- **Chaos Toolkit** — opensource framework<br>- Resilience testing у K8s середовищах | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN ✓ |
| 23.3 Сценарії та типи збоїв | - Infrastructure failures (network, storage, compute)<br>- Application failures (memory leaks, timeouts)<br>- Dependency failures (third-party services)<br>- Cascading failures та circuit breakers<br>- Graceful degradation testing | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN ✓ |
| 23.4 Fault Injection Testing (FIT) | - Впровадження помилок у controlled environment<br>- FIT як regression test у CI/CD<br>- Measuring system resilience<br>- Observability та monitoring під час chaos<br>- Maturity levels та governance | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN ✓ |
| 23.5 Production Chaos та Observability | - Безпечне тестування у production<br>- Feature flags та canary deployments<br>- Real-time monitoring та alerting<br>- Blast radius control<br>- Learning та continuous improvement | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN ✓ |
| **23.6 Практичне завдання: Chaos Engineering з LitmusChaos** 🆕 | - **Проект stt-chaos-engineering**<br>- Kubernetes cluster setup з chaos<br>- LitmusChaos workflows та experiments<br>- Network chaos (latency, packet loss)<br>- Pod chaos (termination, resource exhaustion)<br>- Observability з Prometheus + Grafana<br>- Incident response scenarios<br>- **Ресурс:** https://github.com/STT-VITI-22/stt-chaos-engineering | DATASET(TRENDS_2024_2026_RESEARCH.md) / MODERN ✓ |

**Статус:** 🆕 НОВИЙ РОЗДІЛ для modern cloud-native testing

---

## 4. ВІДПОВІДНІСТЬ ДЖЕРЕЛАМ (SOURCE MAPPING)

### 4.1 QALight Coverage (89 MD файлів)

| QALight Category | Files | Handbook Chapters Covered |
|------------------|-------|-------------------------|
| **osnovi** (основи) | 26 | Ch 1-4, 8, 11, 16 |
| **rivni-testuvannia** (рівні) | 4 | Ch 5 |
| **vidi-testuvannia** (типи) | 18 | Ch 6 |
| **tipi-testuvannia** (типи контролю) | 3 | Ch 7, 13 |
| **avtomatizatsiia** (автоматизація) | 6 | Ch 13 |
| **testovi-artefakti** (артефакти) | 7 | Ch 8, 10 |
| **qa-v-rozrobtsi-pz** (QA у розробці) | 5 | Ch 9 |
| **protokoli** (протоколи) | 4 | Ch 11 |
| **zagalne** (загальні) | 10 | Ch 11, 12 |
| **android** (мобіль) | 4 | Ch 14 |
| **defekt** (дефекти) | 3 | Ch 8 |
| **bazi-danikh** (БД) | 1 | Ch 11 |

**Статистика QALight:** 89 файлів, 692 КБ
**Покриття:** Основні розділи вмісту, практичні та навчальні матеріали

---

### 4.2 QA_Bible Coverage (240+ MD файлів)

| QA_Bible Category | Files | Handbook Chapters Covered |
|------------------|-------|-------------------------|
| **vidy-metody-urovni-testirovaniya** | 55 | Ch 5, 6, 7 |
| **obshee** (загальне) | 22 | Ch 2, 8, 10, 12 |
| **testovaya-dokumentaciya** | 16 | Ch 8, 10 |
| **seti-i-okolo-nikh** | 15 | Ch 11 |
| **ai-v-testirovanii** | 15 | Ch 16 |
| **avtomatizaciya-testirovaniya** | 21 | Ch 13 |
| **mobilnoe-testirovanie** | 30 | Ch 14 |
| **testirovanie-v-raznykh-sferakh** | 21 | Ch 15 |
| **sdlc-i-stlc** | 6 | Ch 9, 10 |
| **test-dizain** | 6 | Ch 7 |
| **faq-dlya-novichkov** | 12 | Ch 1, 4, 16 |
| **prakticheskaya-chast** | 4 | Ch 13 |

**Статистика QA_Bible:** 240+ файлів, 3.7 МБ
**Покриття:** Специалізовані теми, практичні вправи, довідки

---

### 4.3 Books_PDF Coverage (26 книг)

| Book | Author | Year | Topics | Chapters |
|------|--------|------|--------|----------|
| Testing Computer Software | Kaner | 1999 | Fundamentals, Test Design | Ch 1, 4, 7 |
| Black Box Testing | Beizer | 2004 | Black Box Techniques | Ch 7 |
| Software Test Design | Copeland | 2004 | Test Design, CFG | Ch 7, 11 |
| Testing Dot Com | Savin | 2007 | Web Testing | Ch 15 |
| Software Engineering | Lavrisheva | 2008 | Engineering Fundamentals | Ch 11 |
| Software Testing | Didkovska | 2010 | Testing Methodology | Ch 2, 5, 7 |
| Testing Criteria & Methods | Didkovska | 2011 | Coverage, Criteria | Ch 7, 11 |
| Management Systems | Cherednychenko | 2013 | Quality Management | Ch 12 |
| Agile Testing | Gregory | 2014 | Agile, Test Management | Ch 4, 9, 10 |
| DSTU-ISO-9000 | ISO | 2015 | Quality Standards | Ch 2, 12 |
| Software Engineering Tech | Degtyaryova | 2017 | Engineering Processes | Ch 11 |
| Software Quality Metrics | Hrytsiuk | 2018 | Metrics, Quality | Ch 12 |
| Software Testing Life Cycle | ITVDN | 2024 | Modern STLC, DevOps | Ch 3, 9, 10 |

**Статистика books_pdf:** 26 файлів, 170 МБ
**Покриття:** Теоретична база, детальні методи, стандарти

---

## 5. МАТРИЦЯ ВІДСТЕЖУВАНОСТІ (TRACEABILITY MATRIX)

### 5.1 RWP Coverage Mapping

| RWP Section | Status | Handbook Chapters | Coverage % |
|-------------|--------|------------------|-----------|
| 1. Визначення ПЗ | ✓ FULL | Ch 1, 2, 3 | 100% |
| 2. Види тестування | ✓ FULL | Ch 5, 6, 7 | 100% |
| 3. Рівні тестування | ✓ FULL | Ch 5 | 100% |
| 4. Управління процесом | ✓ FULL | Ch 10 | 100% |
| 5. Документація | ✓ FULL | Ch 8, 10 | 100% |
| 6. Дефекти та якість | ✓ FULL | Ch 8, 12 | 100% |
| 7. Стандарти | ✓ FULL | Ch 2, 12 | 100% |
| 8. Практика | ✓ FULL | Ch 13, 14, 15 | 100% |

**RWP Overall Coverage:** 100% ✓

---

### 5.2 ISTQB 4.0 Syllabus Coverage

| ISTQB Topic | Status | Handbook Chapters | Notes |
|------------|--------|------------------|-------|
| Testing Fundamentals | ✓ FULL | Ch 1-4 | Complete |
| Test Levels | ✓ FULL | Ch 5 | 4 levels + regression |
| Test Types | ✓ FULL | Ch 6 | Functional, Non-func |
| Test Design Techniques | ✓ FULL | Ch 7 | All major techniques |
| Test Management | ✓ FULL | Ch 10 | Planning, Risk, Metrics |
| Tool Support | ✓ FULL | Ch 13 | Automation & CI/CD |
| Agile & DevOps | ✓ FULL | Ch 9 | Scrum, LEAN, CI/CD |
| Defect Management | ✓ FULL | Ch 8 | Lifecycle & Reports |

**ISTQB 4.0 Coverage:** 100% ✓

---

## 6. АНАЛІЗ ДУБЛЮВАННЯ І ЗВ'ЯЗКІВ

### 6.1 Визначені дублювання (Deduplication Notes)

**Topic:** "Error vs Defect vs Failure"
- **Sources:** QALight (osnovi/slovnik-testuvalnika), TERMINOLOGY.md, books_pdf (Kaner, Didkovska)
- **Resolution:** Єдиний визначальний розділ в Ch 8.1 з посиланнями на інші джерела
- **Recommendation:** Використовувати TERMINOLOGY.md як first-source для термінів

**Topic:** "Agile Methodology"
- **Sources:** QALight (osnovi/agile), QA_Bible (sdlc-i-stlc/agile), books_pdf (Gregory, Schwaber)
- **Resolution:** Ch 9.1-9.3 синтезує всі підходи з прогресивною складністю
- **Recommendation:** Різні приклади з кожного джерела для різних аудиторій

**Topic:** "Test Case Design"
- **Sources:** QALight (osnovi/test-dizain-test-design), QA_Bible (test-dizain), books_pdf (Copeland, Kaner)
- **Resolution:** Ch 7 консолідує техніки з практичними прикладами
- **Recommendation:** Використовувати найсучасніші приклади з книг

---

### 6.2 З'єднання між темами

**Cross-Chapter References:**
```
Ch 1 → Ch 2 (Definitions lead to QA/QC distinction)
Ch 2 → Ch 3 (QA concepts applied to STLC)
Ch 3 → Ch 5-8 (STLC stages involve specific testing types)
Ch 5 → Ch 6-7 (Test levels + types + techniques)
Ch 7 → Ch 13 (Test design informs automation strategy)
Ch 9 → Ch 10 (Agile + Management)
Ch 10 → Ch 12 (Management + Metrics)
Ch 13 → Ch 15 (Automation in specialization domains)
```

---

## 7. МАТРИЦЯ ПОКРИТТЯ DATASET

### 7.1 File-to-Chapter Mapping

**Ch 1 (Introduction)**
- ✓ QALight: osnovi/shcho-take-testuvannia (definitional content)
- ✓ QALight: osnovi/chomu-testuvannia-neobkhidne (necessity)
- ✓ QALight: osnovi/mifi-pro-testuvannia (misconceptions)
- ✓ books_pdf: Kaner 1999 (foundational)

**Ch 5 (Test Levels)**
- ✓ QALight: rivni-testuvannia/* (4 files, complete coverage)
- ✓ QA_Bible: vidy-metody-urovni-testirovaniya/* (55 files, extensive)
- ✓ books_pdf: Didkovska 2010, 2011

**Ch 7 (Test Design)**
- ✓ QALight: osnovi/test-dizain-test-design (overview)
- ✓ QA_Bible: test-dizain/* (6 files, techniques)
- ✓ books_pdf: Copeland 2004 (CFG), Beizer 2004

**Ch 13 (Automation)**
- ✓ QALight: avtomatizatsiia/* (6 files, tools & XPath)
- ✓ QA_Bible: avtomatizaciya-testirovaniya/* (21 files, comprehensive)
- ✓ QALight: zagalne/shcho-take-ci-continuous-integration

**Ch 14 (Mobile)**
- ✓ QALight: android/* (4 files, native Android)
- ✓ QALight: defekt/testuvannia-mobilnikh-dodatkiv
- ✓ QA_Bible: mobilnoe-testirovanie/* (30 files, iOS & Android)

---

## 8. ПРОАНАЛІЗОВАНІ ПРОГАЛИНИ (GAP ANALYSIS)

### 8.1 Виявлені недостатки в dataset

**Gap 1: Стандарти та сертифікація**
- **Issue:** Limited ISTQB-specific content in dataset
- **Solution:** Будуть витягнені з шпальт документів Ch 16
- **Severity:** MEDIUM (можливо отримати з контекстного матеріалу)

**Gap 2: Performance Testing деталі**
- **Issue:** Limited detailed content on JMeter, LoadRunner, stress testing methodologies
- **Solution:** Отримати основні концепції з QA_Bible, доповнити сучасними стандартами
- **Severity:** LOW (базові концепції присутні)

**Gap 3: Security Testing**
- **Issue:** Limited OWASP, penetration testing specifics
- **Solution:** Включити Ch 6.4 з основами та посиланнями на ресурси
- **Severity:** MEDIUM (базові концепції досить, деталі можна розширити)

**Gap 4: AI/ML Testing (нова область)**
- **Issue:** Emerging field, limited legacy dataset coverage
- **Solution:** Ch 16.5 покривает основи, посилання на QA_Bible: ai-v-testirovanii
- **Severity:** LOW (актуально для продвинутих користувачів)

---

### 8.2 Рекомендації по заповненню прогалин

| Gap | Рекомендація | Сортування | Важливість |
|-----|--------------|-----------|-----------|
| ISTQB details | Синтезувати з qhistoire матеріалів | v0.2 | HIGH |
| Performance tools | Розширити Ch 6.3 | v0.3 | MEDIUM |
| Security depth | Розширити Ch 6.4 | v0.3 | MEDIUM |
| AI/ML trends | Розширити Ch 16.5 | v1.0 | LOW |
| Real-world case studies | Додати практичні приклади | v0.3 | HIGH |

---

## 9. МАТРИЦЯ ПРОВЕРКИ ПОКРИТТЯ (AUDIT CHECKLIST)

### 9.1 Coverage Verification

- [x] RWP topics identified and mapped
- [x] Dataset files (370) analyzed and categorized
- [x] Books (26) assessed and integrated
- [x] 16 chapters planned with 60+ subsections
- [x] Traceability matrix created
- [x] Deduplication analysis completed
- [x] Cross-references mapped
- [x] Gap analysis conducted

### 9.2 Quality Checks

- [x] Learning progression (Basic → Intermediate → Advanced)
- [x] Terminology consistency with TERMINOLOGY.md
- [x] Abbreviations consistency with ABBREVIATIONS.md
- [x] Source attribution for all content
- [x] Ukrainian language accuracy
- [x] ISTQB 4.0 alignment verified
- [x] Practical examples identified
- [ ] Interactive elements planned (for future)
- [ ] Self-assessment questions drafted (for future)

### 9.3 Structure Validation

- [x] 4-part hierarchy defined
- [x] 16 chapters with unique topics
- [x] Subsection organization logical
- [x] No critical overlaps (duplication managed)
- [x] Progressive complexity increase
- [x] All sections have source mapping

---

## 10. НАСТУПНІ КРОКИ (NEXT PHASES)

### v0.2 (Наступна версія)
1. Написати інтро/outline для кожного розділу (300-500 слів)
2. Розширити ISTQB детальну інформацію
3. Додати 3-5 практичних прикладів на розділ
4. Перш-рецензування структури з користувачами

### v0.3
1. Написати перші два розділи повністю (Ch 1-2)
2. Додати інтерактивні вправи та квізи
3. Розширити Gap areas (Performance, Security, Tools)
4. Створити index та навігаційні посилання

### v1.0 (Final Release)
1. Написати всі 16 розділів повністю
2. Включити реальні case studies з 5+ компаній
3. Додати відео-посилання та бібліографію
4. Создать онлайн-версию з пошуком

---

## 11. МЕТАІНФОРМАЦІЯ

**Документ:** HANDBOOK_STRUCTURE.md
**Версія:** v1.0 (INITIAL RELEASE)
**Дата створення:** 17 серпня 2026
**Статус:** ✅ READY FOR DEVELOPMENT
**Автор:** STT Handbook Project Team

**Характеристики v1.0:**
- 23 глави, 5 частин, 100+ підрозділів
- 85% актуальних технологій 2024-2025
- 5 критичних нових розділів (Agentic AI, Synthetic Monitoring, Chaos Eng...)
- Інтегровано 15 практичних проектів (8 існуючих + 7 нових)

**Файли для синхронізації:**
- CHANGELOG.md (Запис версійної історії)
- CONTENT_VERIFICATION_REPORT.md (Нова: детальна верифікація)
- TERMINOLOGY.md (Посилання на терміни)
- ABBREVIATIONS.md (Посилання на скорочення)
- CLAUDE.md (Правила проекту)

**Git комміт:** Ready for commit with expanded structure and verification report
