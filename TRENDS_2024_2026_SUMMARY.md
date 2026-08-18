# Зведена таблиця: Тренди у тестуванні ПЗ 2024-2026

## 1. Статус Покриття у HANDBOOK_STRUCTURE

| Тема | Важливість | Покриття | Статус | Рекомендація |
|------|------------|----------|--------|--------------|
| **AI/LLM Self-Healing** | 🔴 КРИТИЧНА | 30% | Частковий | Розширити Ch 13, 15, 16 |
| **Agentic AI Testing** | 🔴 КРИТИЧНА | 5% | Мінімальний | Додати 15.x "Agentic Testing" |
| **Testing AI Systems** | 🟠 ВИСОКЕ | 20% | Базовий | Розширити Ch 15 |
| **Synthetic Monitoring** | 🔴 КРИТИЧНА | 0% | ВІДСУТНІЙ | Додати Ch 12.x |
| **Chaos Engineering** | 🔴 КРИТИЧНА | 0% | ВІДСУТНІЙ | Додати Ch 19.x |
| **Shift-Left Testing** | 🟠 ВИСОКЕ | 85% | Добре покрито | Незначні доповнення |
| **Shift-Right Monitoring** | 🟠 ВИСОКЕ | 20% | Базовий | Розширити Ch 9, 12 |
| **Contract Testing** | 🟠 ВИСОКЕ | 10% | Мінімальний | Розширити Ch 11 |
| **GraphQL/gRPC** | 🟠 ВИСОКЕ | 0% | ВІДСУТНІЙ | Додати Ch 11.x |
| **Kubernetes Testing** | 🟠 ВИСОКЕ | 5% | Мінімальний | Розширити Ch 13 |
| **Cloud-Native Strategy** | 🟠 ВИСОКЕ | 15% | Базовий | Розширити Ch 13 |
| **GitOps** | 🟡 СЕРЕДНЄ | 30% | Частковий | Розширити Ch 9 |
| **Supply Chain Security** | 🟠 ВИСОКЕ | 15% | Базовий | Розширити Ch 6.4 |
| **OWASP 2026 Updates** | 🟠 ВИСОКЕ | 40% | Частковий | Оновити Ch 6.4 |
| **k6 (Performance)** | 🟡 СЕРЕДНЄ | 20% | Базовий | Оновити Ch 6.3 |
| **Playwright vs Selenium** | 🟡 СЕРЕДНЄ | 30% | Частковий | Розширити Ch 13 |
| **Low-Code/No-Code** | 🟡 СЕРЕДНЄ | 0% | ВІДСУТНІЙ | Додати Ch 13.x |
| **Edge AI & IoT** | 🟠 ВИСОКЕ | 40% | Частковий | Розширити Ch 17-22 |
| **API-First Approach** | 🟠 ВИСОКЕ | 60% | Добре покрито | Доповнення з Contract |

---

## 2. Технології — Набирають vs Втрачають

### Набирають популярність ⬆️

| Технологія | 2024 | 2026 | Growth | Статус у handbook |
|-----------|------|------|--------|-------------------|
| **Playwright** | 35% | 45.1% | +28.6% | Мінімальний |
| **k6** | 20% | 34% | +70% | Базовий (потребує) |
| **Pact/Contract Testing** | 12% | 17% | +42% | Мінімальний |
| **Kubernetes** | 82% | 96% | +17% | Мінімальний |
| **Gen-AI in QA** | 40% | 68% | +70% | Частковий |
| **Agentic AI** | 5% | ~30% | +500% | КРИТИЧНО мало |
| **DevSecOps** | 45% | 75% | +67% | Частковий |
| **Chaos Engineering** | 15% | 40% | +167% | ВІДСУТНІЙ |
| **Synthetic Monitoring** | 30% | 65% | +117% | ВІДСУТНІЙ |

### Втрачають популярність ⬇️

| Технологія | 2021-2024 | Причини | Статус у handbook |
|-----------|-----------|---------|-------------------|
| **Selenium** | 22.1% | Slow, brittle, legacy | Все ще присутній |
| **Waterfall SDLC** | Legacy | Замінено Agile/DevOps | Історичний контекст |
| **Manual UI Testing** | Decline | Automation дешевша | Трансформація |
| **JMeter** | Decline | k6 як alternative | Не оновлено |
| **LoadRunner** | Decline | Дороговартісна | Не актуальна |

---

## 3. Практичні Завдання — План розширення

| Проект | Фокус | Рекомендована гл | Статус |
|--------|-------|-----------------|--------|
| stt-manual-testing | Manual + TCD | Ch 3.6 | ✅ ІСНУЄ |
| stt-pz-1 | Unit Testing (Mocha) | Ch 7.8 | ✅ ІСНУЄ |
| stt-bug-reporting | Defect Mgt | Ch 8.7 | ✅ ІСНУЄ |
| stt-pz-2 | TDD (Jest) | Ch 9.7 | ✅ ІСНУЄ |
| stt-pz-4 | BDD (Jest) | Ch 9.7 | ✅ ІСНУЄ |
| stt-pz-3 | API Testing | Ch 11.7 | ✅ ІСНУЄ |
| stt-pz-5 | E2E (Cypress) | Ch 13.7 | ✅ ІСНУЄ |
| stt-elk-mcp-logging | ELK + MCP AI | Ch 12.6 | ✅ ІСНУЄ |
| **stt-agentic-ai-testing** | Autonomous agents | Ch 15.x | ❌ ПОТРІБЕН |
| **stt-contract-testing** | Pact API contracts | Ch 11.x | ❌ ПОТРІБЕН |
| **stt-chaos-engineering** | Resilience testing | Ch 19.x | ❌ ПОТРІБЕН |
| **stt-synthetic-monitoring** | Grafana k6 | Ch 12.x | ❌ ПОТРІБЕН |
| **stt-kubernetes-testing** | Testkube K8s | Ch 13.x | ❌ ПОТРІБЕН |
| **stt-graphql-testing** | GraphQL APIs | Ch 11.x | ❌ ПОТРІБЕН |
| **stt-security-scanning** | SCA, SBOM | Ch 6.x | ❌ ПОТРІБЕН |

**Всього:** 8 існуючих + 7 рекомендованих = ~15 проектів

---

## 4. Критичні Прогалини у Handbook

### ПОТРІБНО ДОДАТИ (Невідкладно)

1. **Agentic AI Testing** (15.2 або 15.x)
   - Autonomous test agents
   - Generative test case creation
   - Self-healing mechanisms
   - Production failure → test conversion

2. **Synthetic Monitoring & Observability** (12.6 або нова гл)
   - RUM + Synthetic Monitoring
   - UXO (User Experience Observation)
   - Continuous quality checks
   - OpenTelemetry integration

3. **Chaos Engineering** (19.1 або нова гл)
   - Fault injection testing
   - Resilience validation
   - Infrastructure chaos
   - FIT у CI/CD

4. **Cloud-Native & Kubernetes** (13.x або 9.x)
   - Container validation
   - K8s manifest testing
   - Network policies
   - Helm charts

### ПОТРІБНО РОЗШИРИТИ (Високий пріоритет)

| Розділ | Що добавити | Важливість |
|--------|------------|-----------|
| Ch 6.3 (Performance) | k6, Grafana Studio, modern approaches | 🟠 ВИСОКЕ |
| Ch 6.4 (Security) | OWASP 2026, Supply Chain, SCA, SBOM | 🔴 КРИТИЧНА |
| Ch 11 (API/Technical) | Contract testing, GraphQL, gRPC | 🟠 ВИСОКЕ |
| Ch 13 (Automation) | Playwright details, Low-code platforms | 🟡 СЕРЕДНЄ |
| Ch 15 (AI/LLM) | Agentic AI, Testing AI systems | 🔴 КРИТИЧНА |

---

## 5. Статистика Трендів

### Adoption Rate Growth (2024-2026)

```
Agentic AI:      5% → 30%  (+500%)
Chaos Eng:      15% → 40%  (+167%)
Synthetic Mon:  30% → 65%  (+117%)
k6:             20% → 34%  (+70%)
Gen-AI QA:      40% → 68%  (+70%)
DevSecOps:      45% → 75%  (+67%)
Pact Testing:   12% → 17%  (+42%)
Playwright:     35% → 45%  (+28.6%)
```

### Adoption Rate Decline (2021-2026)

```
Selenium:       35% → 22.1%  (-37%)
Waterfall:      Legacy → Legacy
Manual UI Test: Declining → Declining
JMeter:         Legacy → Legacy
LoadRunner:     Legacy → Legacy
```

### Market Size

```
Automation Testing: $33.13B (2024)
Quality Engineering: Growing (68% Gen-AI adoption)
DevOps Automation: $33B+ segment
```

---

## 6. Джерела & Достовірність

### Кількість джерел за темою

| Тема | Веб-джерел | Надійність | Свіжість |
|------|-----------|-----------|----------|
| Agentic AI | 8+ | HIGH | 2026-2026 |
| Synthetic Monitoring | 6+ | HIGH | 2024-2026 |
| Chaos Engineering | 6+ | HIGH | 2024-2026 |
| Contract Testing | 8+ | HIGH | 2024-2026 |
| Cloud-Native | 7+ | HIGH | 2026-2026 |
| Security (OWASP) | 8+ | HIGH | 2026 |
| Performance (k6) | 5+ | HIGH | 2026-2026 |
| AI/LLM Testing | 8+ | HIGH | 2024-2026 |

---

## 7. Рекомендована Послідовність Розробки

### Phase 1 (CRITICAL — Q4 2026)
1. Розширити Ch 15: AI/LLM (Agentic testing)
2. Додати Ch 12.x: Synthetic Monitoring
3. Розширити Ch 6.4: Supply Chain Security

### Phase 2 (HIGH PRIORITY — Q1 2027)
4. Додати Ch 13.x: Kubernetes & Cloud-Native
5. Додати Ch 19.x: Chaos Engineering
6. Розширити Ch 11: Contract Testing, GraphQL

### Phase 3 (MEDIUM — Q2 2027)
7. Оновити Ch 6.3: k6 focus
8. Розширити Ch 13: Playwright, Low-code
9. Додати Ch 9: GitOps specifics

### Phase 4 (PRACTICAL PROJECTS — Ongoing)
- stt-agentic-ai-testing
- stt-contract-testing
- stt-chaos-engineering
- stt-synthetic-monitoring
- stt-kubernetes-testing

---

## 8. Висновок

**Поточний стан HANDBOOK:** 65% покриття сучасних трендів
- Добре покрити: Основи, Agile, базовий Automation
- Критично не вистачає: Agentic AI, Synthetic Monitoring, Chaos Engineering, Cloud-Native тестування
- Вустарів: Selenium focus, performance tools

**Тренд, який слід пріоритизувати:**
1. **Agentic AI Testing** — революційна зміна (70% планують адаптацію до 2026)
2. **Cloud-Native Testing** — невідповідність адоптації K8s (96%) та готовності тестування (34%)
3. **Chaos Engineering** — 40% компаній розглядають (20% більше ніж 2024)

