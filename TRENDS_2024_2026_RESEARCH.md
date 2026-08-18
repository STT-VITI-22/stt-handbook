# Дослідження актуальних трендів у тестуванні ПЗ — 2024-2026

**Дата дослідження:** 18 серпня 2026  
**Джерела:** 25+ веб-джерел, CNCF, Gartner, Forrester, GitHub, Medium, Industry reports  
**Охоплені теми:** AI/LLM, Shift-Left/Right, Contract Testing, Synthetic Monitoring, Chaos Engineering, Cloud-Native, Security, Performance, IoT, DevOps/GitOps

---

## EXECUTIVE SUMMARY

### Основні висновки

1. **AI/LLM революція у тестуванні** — від асистента до автономного агента
   - Self-healing тести вже в production
   - Agentic AI тестування (70% компаній планують до 2026)
   - Генерація тест-дизайну через промпти

2. **Біфуркація підходів**: Shift-Left + Shift-Right стають комплементарними
   - Левий крок: Раннє перехоплення дефектів
   - Правий крок: Monitoring та learning у production

3. **Новий стандарт інфраструктури**: Cloud-Native + Kubernetes
   - 96% адаптовано Kubernetes (але лише 34% адаптували тестування!)
   - API-first підходи замість UI-centered
   - Contract testing стає best practice (lишаючись рідкісним — 17%)

4. **Security як перший клас громадянина**: OWASP Top 10  2026
   - Supply Chain Failures (NEW) — #3 у рейтингу
   - DevSecOps у CI/CD pipeline (48% reduction MTTR)

5. **Закат інструментів старого покоління**:
   - Selenium: 22.1% adoption (падіння)
   - Playwright: 45.1% adoption (+14% YoY)
   - Cypress: 14.4% adoption (стабільна ніша)

6. **Новий інструментарій**:
   - k6 — замість JMeter для cloud-native
   - Pact/PactFlow — для contract testing
   - Testkube — для Kubernetes
   - Grafana k6 Studio (low-code)

---

## 1. AI/LLM ИСПОЛЬЗОВАНИЕ В ТЕСТИРОВАНИИ

### 1.1 Selbst-Healing Tests (Самодиагностирующиеся Тесты)

**Поточний стан:**
- Вже в production у forward-thinking компаніях
- Комбінація LLM + традиційних фреймворків
- Тести автоматично фіксять себе при zmіні локаторів
- 88% reduction в maintenance costs (порівняно з ручним)

**Як працює:**
```
Крок 1: Тест падає (локатор неактуальний)
Крок 2: LLM аналізує сторінку, знаходить новий локатор
Крок 3: Тест оновлюється та перезапускається
Крок 4: Результат логується для auditing
```

**Інструменти:**
- Virtuoso QA
- TestGrid с AI enhancement
- Playwright з Claude/GPT-4 інтеграцією
- Custom MCP-based solutions (як у stt-elk-mcp-logging)

**Статус у handbook:** ВМІСЦЕНО (Ch 13, 16)

---

### 1.2 Gen-AI для Test Design та Generation

**Поточний стан:**
- 9x faster test creation (LLM vs. manual)
- Fine-tuned моделі можуть генерувати целові тест-сценарії

**Приклади:**
```
Input:  "Login form з username і password"
Output: [Valid login, Invalid credentials, 
         Session timeout, SQL injection]
```

**Компанії що внедрили:**
- Meta (TestGen-LLM)
- SmartBear (HaloAI integration)
- CloudQA
- Capgemini (68% adoption Gen AI у QA)

**Рівень покриття в handbook:** ЧАСТКОВИЙ (Ch 15, 16)
- Потребує розширення в Ch 16 (AI/LLM Testing)

---

### 1.3 Agentic AI Testing — РЕВОЛЮЦІЙНИЙ ТРЕНД

**Що це:**
Автономні AI агенти, які:
- Аналізують user stories
- Генерують тест-кейси
- Виконують тести у різних оточеннях
- Діагностують failure причини
- Самодиагностуються (self-heal)
- Конвертують production failures у тесты (shift-right loop)

**Темп адаптації:**
- 2024: < 5% компаній
- 2026: Forrester ренеймував категорію на "Autonomous Testing Platforms"
- Проекція 2026: 40% enterprise apps
- Проекція 2028: 33% enterprise software

**Економічний вплив:**
- Manual тестування: $2.3M/рік
- Agentic AI: скорочення на 30-40% + 2-3x faster release cycles

**Рівень покриття в handbook:** МІНІМАЛЬНИЙ (Ch 15 згадує, но не детально)
- **КРИТИЧНА ПОТРЕБА:** Додати нову секцію "Agentic AI Testing" в Ch 15

---

### 1.4 Testing AI Systems — Зворотна сторона

**Нові виклики:**
1. **Non-determinism** — LLM outputs не гарантовані
2. **Test Oracle Problem** — як перевірити "правильність" AI відповіді?
3. **Hallucination Testing** — виявлення вигаданих результатів
4. **Prompt Injection Attacks** — безпека LLM
5. **Metamorphic Testing** — нова техніка для AI

**Методи перевірки AI:**
- Confusion Matrix (для класифікаторів)
- Red Teaming (для jailbreaks)
- Hallucination detection
- Edge case collection

**Статус:** ПОТРЕБУЄ РОЗШИРЕННЯ В HANDBOOK
- Ch 15 має базову інформацію
- Ch 16 може мати спеціалізовану секцію

---

## 2. SHIFT-LEFT ТА SHIFT-RIGHT СТРАТЕГІЇ

### 2.1 Shift-Left Testing (Раннє тестування)

**Поточні підходи:**
- Early QA involvement (з requirements gathering)
- Unit + Contract tests на pre-commit
- Security testing в development (Shift-Left Security)
- TDD/BDD у спринтах

**Інструменти:**
- Pre-commit hooks
- IDE plugins (Kover, JaCoCo для code coverage)
- SAST tools (SonarQube, Checkmarx)

**Статус у handbook:** ✅ ПОВНІСТЮ ПОКРИТО
- Ch 3 (STLC phases)
- Ch 7 (TDD/BDD techniques)
- Ch 9 (Agile/DevOps integration)

---

### 2.2 Shift-Right Testing (Production Monitoring)

**Поточні підходи:**
1. **Synthetic Monitoring** — імітація user actions в production
2. **User Experience Observation (UXO)** — комбінація RUM + synthetic
3. **Production Defect Detection** — AI для пошуку аномалій
4. **Continuous Learning** — production failures → нові тести

**Взаємодія Shift-Left + Shift-Right (2026-2026):**
```
Development:        Production:
TDD/BDD ← → Synthetic Monitoring
Contract Tests ← → RUM (Real User Monitoring)
Chaos Testing ← → Chaos Experiments
AI Agents ← → AI-powered Alerting
```

**Інструменти:**
- Grafana k6 (Synthetic Monitoring + Load Testing)
- Datadog, New Relic (Observability)
- PagerDuty (Alerting)
- OpenTelemetry (Standardized instrumentation)

**Статус у handbook:** БАЗОВИЙ (Ch 9, 12)
- Потребує детальної секції у Ch 12 (Metrics & Quality)

---

## 3. CONTRACT TESTING ТА API-FIRST ПІДХОДИ

### 3.1 Contract Testing — Критична статистика

**Gap у галузі:**
- 82% компаній адаптували API-first підходи
- Але лишень 17% використовують contract testing
- **Результат:** Невловлені breaking changes на integration етапі

**Чому важливо:**
- Elite performers 2.6x більше ймовірно використовують contract testing
- Contract tests у CI/CD запускаються до production
- Consumer-driven contracts (Pact) — інду-стандарт

**Підходи:**
1. **Pact** — Consumer-driven (JavaScript, Java, Go, Python)
2. **Contract-first development** — Shared API specs (OpenAPI/AsyncAPI)
3. **Schema validation** — JSON Schema за API responses
4. **API mocking** — для parallel frontend/backend development

**Інструменти:**
- Pact Flow (AI-augmented)
- SmartBear (HaloAI integration)
- Postman (contract tests)
- Dredd, OpenAPI validators

**Статус у handbook:** МІНІМАЛЬНИЙ
- Згаданий у Ch 11 (API testing) але без contract specifics
- **Потреба:** Розширення гл 11, можливо додати практичне завдання

---

### 3.2 GraphQL та gRPC Testing

**Нові протоколи требуют нових підходів:**
- GraphQL: Query complexity analysis, field-level permissions
- gRPC: Binary protocol, streaming, load testing specifics

**Рівень покриття:** ВІДСУТНІЙ у handbook
- Лише базові REST API (Ch 11)
- **Критична потреба:** Додати Ch 11.x про GraphQL/gRPC

---

## 4. SYNTHETIC MONITORING І OBSERVABILITY

### 4.1 Поточний стан

**Тренд:**
- 65% компаній систематично внедрили observability
- User Experience Observation (UXO) — комбінація RUM + synthetic
- Synthetic monitoring як continuous quality check

**Компоненти:**
1. **Browser-based testing** — headless Chrome/Playwright
2. **API monitoring** — endpoint availability
3. **Mobile app testing** — синтетичні user journeys
4. **Custom script support** — JavaScript для складних scenario

**Інтеграція з OpenTelemetry:**
- Синтетичні тести можуть корелюватися з backend traces
- Unified visibility в Grafana, Datadog, NewRelic

**Інструменти:**
- Grafana Cloud Synthetic Monitoring (+ k6)
- Uptrace
- Checkly
- Datadog Synthetic

**Статус у handbook:** ВІДСУТНІЙ
- Лишень згадка у Ch 9 (DevOps)
- **Потреба:** Нова секція у Ch 12 (Metrics) або окремий підрозділ

---

## 5. CHAOS ENGINEERING І RESILIENCE TESTING

### 5.1 Прорив у адаптації

**Статистика:**
- Gartner 2026: 40% компаній розглядають chaos engineering
- 2026 вартість downtime: $5,600/хвилину
- Харнес (Harness) випустив 2024 features: ChaosGuard, automated K8s onboarding

**Підхід:**
```
Fault Injection → System Response → Recovery Validation
```

**Типи тестів:**
1. **Network chaos** — latency, packet loss
2. **Resource chaos** — CPU, memory exhaustion
3. **Infrastructure chaos** — node failures
4. **Application chaos** — service timeouts
5. **FIT (Fault Injection Testing)** — у CI/CD як regression check

**AI Integration:**
- AI-powered experiment design
- Intelligent fault scenario generation
- Pattern detection у failures

**Інструменти:**
- Harness Chaos Engineering
- Gremlin
- LitmusChaos
- Chaos Toolkit

**Статус у handbook:** ВІДСУТНІЙ ПОВНІСТЮ
- **Критична потреба:** Додати новий підрозділ (можливо Ch 19 в Part V або Ch 12.x)

---

## 6. CLOUD-NATIVE ТЕСТУВАННЯ

### 6.1 Kubernetes Adoption vs Testing Maturity Gap

**Критична статистика:**
- 96% компаній використовують або evaluating Kubernetes
- 82% production K8s adoption (2026 CNCF survey)
- Але: Лишень 34% адаптували тестову стратегію!

**Виклики:**
- Ephemeral containers
- Network policies, service discovery
- Helm charts, manifests validation
- Configuration drift

**Що тестувати:**
1. **Container layer** — image scanning, vulnerabilities
2. **Orchestration layer** — manifest correctness, Helm charts
3. **Network policies** — service connectivity
4. **Persistence** — data consistency

**Інструменти:**
- Testkube — K8s-native test orchestration
- Signadot — microservices testing
- Conftest — policy testing for configs
- KubeConf/Sonobuoy — cluster compliance

**Статус у handbook:** ВІДСУТНІЙ
- Лишень згадка у Ch 9 (DevOps)
- **Потреба:** Нова секція у Ch 13 (Automation) або окремий підрозділ

---

### 6.2 K8s як "OS for AI"

**Нове явище (2026):**
- Kubernetes стає стандартом для AI/ML deployment
- 82% K8s users розгортають AI models
- New testing needs: model inference, GPU resource allocation

**Статус:** ПОТРЕБУЄ ПОКРИТТЯ
- Ch 15 (AI Testing) може мати K8s specifics

---

## 7. SECURITY TESTING — OWASP EVOLUTION

### 7.1 OWASP Top 10 2026 — Major Changes

**NEW CATEGORY #3: Software Supply Chain Failures**
```
Previous (2021): "Vulnerable and Outdated Components"
New (2026): Broader scope → dependencies + build systems + distribution
```

**Чому це важливо:**
- Log4J, XZUtils, Shai-Hulud (2026 npm worm) — масивні impact
- Shai-Hulud: First self-propagating npm worm (500+ packages скомпрометовані)
- Highest average exploit score серед TOP-10

**Рекомендації для тестування:**
1. **Dependency scanning** — automated SCA (Software Composition Analysis)
2. **Supply chain verification** — signed packages, trusted sources
3. **Build system security** — CI/CD pipeline integrity
4. **Unmaintained library detection** — continuous monitoring

**Інструменти:**
- Snyk, Aqua, Checkmarx (SCA)
- Sigstore (code signing)
- Syft (SBOM generation)
- OpenSSF tools

**DevSecOps в CI/CD:**
- Teams automating security checks: 48% reduction MTTR
- Security gates у pipeline

**Статус у handbook:** БАЗОВИЙ
- Ch 6.4 має OWASP basics
- **Потреба:** Розширення з supply chain specifics

---

## 8. PERFORMANCE ТА LOAD TESTING — СУЧАСНІ ПІДХОДИ

### 8.1 Переход від JMeter до k6

**Тренд:**
- JMeter: Legacy tool (все ще використовується, але...)
- k6: Modern choice для cloud-native (+14% adoption YoY)
- Gatling: Спеціалізований (Scala-based, дорогий)
- Locust: Python-based (developer-friendly)

**k6 переваги:**
- Go-based engine (high performance)
- JavaScript scripting (accessible for web devs)
- Cloud-native architecture
- k6 Studio (new, GUI-based, low-code)
- OpenTelemetry integration

**Тренд:**
```
Traditional: GUI-based, QA-only
Modern: CLI-first, Developer-friendly, CI/CD-native
```

**Граафна k6 Studio (2026):**
- Low-code UI
- Record & playback
- Built-in observability
- Merge with Synthetic Monitoring

**Статус у handbook:** БАЗОВИЙ
- Ch 6.3 має базовий performance testing
- Tools章節відстав (JMeter, LoadRunner, але не k6)
- **Потреба:** Оновлення інструментів

---

## 9. IoT ТА EMBEDDED TESTING

### 9.1 Edge AI як Гарячий Тренд

**Поточний стан:**
- 18.8 billion IoT devices (2024 end)
- Edge AI integration — training на edge замість cloud
- Hardware simulation SDKs для тестування без фізичних пристроїв
- Embedded World 2024-2026: EdgeAI як мейнстрім

**Нові тестові вимоги:**
1. **AI model inference testing** — на обмежених ресурсах
2. **Hardware-in-the-Loop (HIL)** — симуляція сенсорів
3. **Network resilience** — WiFi/MQTT disconnect scenarios
4. **Power consumption** — енергоспоживання при тестуванні

**Інструменти:**
- Advantech EdgeAI SDK
- NEXCOM AIC OT-X
- Qualcomm testing platforms
- TensorFlow Lite на мікроконтролерах

**Статус у handbook:** ВМІСЦЕНО В PART V (Ch 17-22)
- Но: 30-50% покриття (потребує доповнення)
- **Потреба:** Розширення з AI-specific scenarios

---

## 10. DevOps/GitOps ІНТЕГРАЦІЯ

### 10.1 GitOps як усталений стандарт

**Тренд:**
- 2024: GitOps переходить з ніші в mainstream
- Git as single source of truth для infrastructure
- Automated testing як частина GitOps pipeline
- Argo CD, Flux як популярні інструменти

**Testing у GitOps:**
```
Git Commit → Automated Tests (Unit, Integration)
           → Policy checks (Conftest, OPA)
           → Deployment Tests (Helm validation)
           → Integration/E2E Tests
           → GitOps Sync → Observability
```

**Важлива статистика:**
- 83% developers залучені в DevOps activities
- Automation testing market: $33.13B (2024)
- DevSecOps adoption: continuous security у CI/CD

**Популярні tools:**
- GitHub Actions (cloud-native)
- GitLab CI
- Jenkins (legacy, але популярний)
- Argo CD (K8s-native)
- HashiCorp stack (Terraform + vault)

**Статус у handbook:** ДОБРО ПОКРИТО
- Ch 9 (Agile/DevOps)
- Ch 13 (Automation + CI/CD)
- **Потреба:** GitOps specific section

---

## 11. ТРЕНДИ, ЩО ВТРАТИЛИ ПОПУЛЯРНІСТЬ

### 11.1 Selenium Decline

**Статистика:**
- 2021-2024: 22.1% adoption (падіння)
- Причини:
  - Slow execution
  - Brittle scripts (без self-healing)
  - Legacy API
  - Waterfall-style UI-only approach

**Де ще використовується:**
- Legacy projects
- Низькі вимоги до maintenance
- Teams з Selenium expertise

**Статус:** DEPRECATED у новых проектах, але ще присутній в handbook
- Ch 13 має приклади Selenium
- **Рекомендація:** Додати примітку про decline, рекомендувати Playwright/Cypress

---

### 11.2 Waterfall SDLC

**Тренд:**
- Agile/DevOps превалюють
- Waterfall ← для legacy, regulatory (finance, healthcare)
- Комбіновані моделі (SAFe, DAD) — реальність

**Статус у handbook:** ІСТОРИЧНИЙ
- Ch 2, 3 мають Waterfall как базовый контекст
- Але: Focus на Agile (Ch 9)

---

### 11.3 Manual UI Testing (де це можливо)

**Тренд:**
- Automation is new default (Shift-Left)
- Manual testing → Exploratory + UX testing
- UI automation дешевше ніж manual (economically)

**Статус:** ТРАНСФОРМАЦІЯ, а не крах
- Ch 13 має automation focus
- Ch 3 має практичне завдання для manual (stt-manual-testing)

---

## 12. ТЕХНОЛОГІЇ, ЩО НАБИРАЮТЬ ТЕМП

### 12.1 Playwright (vs Selenium)

**Статистика 2026-2026:**
- Adoption: 45.1% (vs Selenium 22.1%)
- Retention: 94% (highest)
- Satisfaction: 92%
- Growth: +14% YoY (State of JS 2026)

**Переваги:**
- Modern API design
- Out-of-box stability (self-healing via locators)
- Multi-browser support
- Trace & debug tools
- Native Playwright Inspector

**Статус у handbook:** МІНІМАЛЬНИЙ
- Лишь згадка в Ch 13
- **Потреба:** Розширення як alternative to Selenium

---

### 12.2 Pact + Contract Testing

**Adoption growth:**
- 2024: 17% teams
- 2026-2026: Growing trend
- PactFlow: AI-augmented approach

**Статус у handbook:** МІНІМАЛЬНИЙ
- Лишень базова інформація у Ch 11
- **Критична потреба:** Додати практичне завдання

---

### 12.3 Low-Code/No-Code Testing Platforms

**Прогноз 2024:** 65% market share
**Статус у handbook:** ВІДСУТНІЙ
- **Потреба:** Огляд platforms (Testim, Applitools, etc.)

---

## 13. MAPPING ДО HANDBOOK_STRUCTURE

### Що ДОБРО ПОКРИТО:
- Ch 1-4: Introduction & Fundamentals ✅
- Ch 5-8: Core Testing Theory ✅
- Ch 9: Agile/DevOps (базовий) ✅
- Ch 13: Automation (але застарів) ⚠️
- Ch 14: Mobile ✅
- Ch 15: AI/LLM (базовий) ⚠️
- Ch 16: Career ✅

### Що КРИТИЧНО БРАКУЄ:

| Тема | Важливість | Рекомендована локація |
|------|------------|----------------------|
| **Agentic AI Testing** | 🔴 КРИТИЧНА | Ch 15 розширення |
| **Synthetic Monitoring** | 🔴 КРИТИЧНА | Ch 12 або нова секція |
| **Chaos Engineering** | 🔴 КРИТИЧНА | Ch 19 (Part V) або Ch 12 |
| **Contract Testing** | 🟠 ВИСОКЕ | Ch 11 розширення |
| **Kubernetes Testing** | 🟠 ВИСОКЕ | Ch 13 розширення |
| **GraphQL/gRPC Testing** | 🟠 ВИСОКЕ | Ch 11 розширення |
| **Cloud-Native Strategy** | 🟠 ВИСОКЕ | Ch 13 або нова гл |
| **GitOps Specific** | 🟡 СЕРЕДНЄ | Ch 9 розширення |
| **Supply Chain Security** | 🟠 ВИСОКЕ | Ch 6.4 розширення |
| **Performance (k6 focus)** | 🟡 СЕРЕДНЄ | Ch 6.3 оновлення |
| **Testing AI Systems** | 🟠 ВИСОКЕ | Ch 15 розширення |
| **Low-Code/No-Code** | 🟡 СЕРЕДНЄ | Ch 13 додання |

---

## 14. ПРАКТИЧНІ ЗАВДАННЯ, ЩО БРАКУЮТЬ

Базуючись на дослідженні, рекомендовані нові практичні проекти:

| Проект | Фокус | Кількість дотепер |
|--------|-------|---|
| **stt-agentic-ai-testing** | Autonomous agents, self-healing | ❌ ПОТРІБЕН |
| **stt-contract-testing** | Pact, API contracts | ❌ ПОТРІБЕН |
| **stt-chaos-engineering** | Chaos testing, resilience | ❌ ПОТРІБЕН |
| **stt-synthetic-monitoring** | Grafana k6, synthetic tests | ❌ ПОТРІБЕН |
| **stt-kubernetes-testing** | K8s integration, Testkube | ❌ ПОТРІБЕН |
| **stt-graphql-testing** | GraphQL specific testing | ❌ ПОТРІБЕН |
| **stt-supply-chain-security** | SBOM, SCA, signed artifacts | ❌ ПОТРІБЕН |

Поточних: 8 проектів
Рекомендованих: +7 (всього ~15)

---

## 15. ВИСНОВКИ ТА РЕКОМЕНДАЦІЇ

### Основні тренди (2024-2026):

1. **🤖 AI/LLM — від асистента до агента**
   - Self-healing вже звичайне явище
   - Agentic AI буде мейнстрімом до 2026
   - Testing AI систем — нова дисципліна

2. **🔀 Shift-Left + Shift-Right — комплементарні, не конкуруючі**
   - Одночасна адоптація: 68% компаній
   - Замикання loop: production failures → нові тесты

3. **🔗 API-first + Contract Testing — інду-стандарт**
   - 82% адаптували API-first
   - 17% використовують contract testing (gap!)
   - Pact + OpenAPI — де рухається галузь

4. **☁️ Cloud-Native тестування — невідповідність адоптації та готовності**
   - 96% Kubernetes adoption
   - 34% адаптували тестування (!=)
   - K8s як OS for AI — новое явление

5. **🔓 Security Testing Shift-Left**
   - Supply Chain failures — новый TOP-10 OWASP категорія
   - DevSecOps у pipeline — норма для elite teams
   - 48% faster MTTR з automation

6. **⚙️ Chaos Engineering стає мейнстрімом**
   - 40% компаній розглядають адоптацію
   - FIT (Fault Injection Testing) як regression check
   - AI-powered scenario generation

7. **📊 Observability + Synthetic Monitoring**
   - UXO (User Experience Observation) — новый фокус
   - 65% компаній систематичний observability
   - OpenTelemetry як стандарт

8. **🚀 Інструментальна революція**
   - Selenium: 22% adoption (падіння)
   - Playwright: 45% adoption (зростання +14% YoY)
   - k6: Новий стандарт для performance
   - Testkube: K8s-native test orchestration

### Рекомендації для HANDBOOK:

#### CRITICAL (Невідкладно):
1. **Розширити Ch 15: AI/LLM Testing**
   - Agentic AI Testing (детально)
   - Testing AI Systems (hallucination, metamorphic)
   - Self-healing specifics

2. **Додати Ch 13.x: Cloud-Native Testing**
   - Kubernetes testing strategy
   - Container validation
   - Network policies

3. **Додати Ch 12.x: Synthetic Monitoring & Observability**
   - Synthetic test design
   - User Experience Observation
   - OpenTelemetry integration

4. **Розширити Ch 6.4: Supply Chain Security**
   - OWASP 2026 updates
   - SCA, SBOM, dependency scanning
   - Build system security

#### HIGH PRIORITY (Скоро):
5. Розширити Ch 11: Contract Testing + GraphQL/gRPC
6. Додати Ch 19.x (Part V): Chaos Engineering
7. Оновити Ch 6.3: k6 як modern alternative для performance testing
8. Додати практичні завдання: stt-agentic-ai, stt-contract-testing, stt-chaos-engineering

#### MEDIUM PRIORITY:
9. Додати GitOps specifics у Ch 9
10. Додати низькокодові платформи у Ch 13
11. Оновити Ch 13 з Playwright/Cypress specifics
12. Додати testing pyramid з cloud-native фокусом

#### DEPRECATED/LEGACY:
- Зберегти Selenium у Ch 13, но додати примітки про decline
- Waterfall залишити для історичного контексту
- Manual UI testing трансформувати на exploratory + UX focus

---

## 16. ДЖЕРЕЛА ДОСЛІДЖЕННЯ

### Веб-джерела (25+):
- CloudQA, TestGrid, Virtuoso QA
- GitHub: awesome-ai-testing
- Medium: множество статей від industry experts
- BrowserStack, Accelq, ContextQA, Qable
- Harness (Chaos Engineering)
- CNCF Annual Survey 2024-2026
- Gartner, Forrester, Capgemini reports
- OWASP (MCP Top 10, A03 2026)
- Signadot, Testkube (K8s testing)
- Grafana Labs (Observability trends)
- SmartBear, Pact Foundation

### Критерії для класифікації трендів:
- Adoption rate
- Investment trends (funding)
- Conference presence (KubeCon, ChaosCarnival, ObservabilityCON)
- Gartner/Forrester quadrant positioning
- Market size та growth rate
- Community sentiment
- Enterprise adoption (Fortune 500)

---

**Документ завершено: 18 серпня 2026**
**Статус: Готово для інтеграції у HANDBOOK_STRUCTURE.md v3.0**

