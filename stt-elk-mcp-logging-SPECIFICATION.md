# stt-elk-mcp-logging: ELK + MCP AI Logging Analysis

**Практичне завдання:** AI-Powered Log Analysis та Monitoring з ELK та MCP сервером

**GitHub:** https://github.com/STT-VITI-22/stt-elk-mcp-logging 🆕

**Розділ посібника:** Chapter 12.6 (нова підтема у "Метрики та оцінювання якості") або окремий advanced розділ

**Рівень складності:** Advanced/Expert

**Тривалість:** 3-4 тижні

**Тип:** Logging + AI Analysis + Monitoring

---

## 1. ОБЗОР ЗАВДАННЯ

### Мета
Навчити студентів:
1. Розгортати та налаштовувати ELK стек (Elasticsearch, Logstash, Kibana) у Docker
2. Генерувати та аналізувати логи з додатків
3. Інтегрувати MCP (Model Context Protocol) сервер для AI-powered log analysis
4. Використовувати Claude AI через MCP для:
   - Автоматичного виявлення аномалій у логах
   - Діагностики проблем
   - Рекомендацій щодо оптимізації

### Контекст
- **ELK Stack**: Стандартна система для логування та моніторингу в enterprise
- **MCP**: Дозволяє AI моделям (Claude) анаізувати великі обсяги даних безпосередньо
- **Практичність**: Студенти дізнаються про modern observability practices

---

## 2. ДЕТАЛІ ПРАКТИЧНОГО ЗАВДАННЯ

### 2.1 Вимоги успіху

**Обов'язкові:**
- ✅ Розгорнути ELK стек через docker-compose
- ✅ Налаштувати Elasticsearch, Logstash, Kibana
- ✅ Створити 2+ додатків, що генерують логи (Python/Node.js)
- ✅ Налаштувати Logstash pipelines для парсингу логів
- ✅ Створити Kibana dashboards (мінімум 3)
- ✅ Інтегрувати MCP сервер для AI аналізу
- ✅ Реалізувати рутини аналізу логів через AI (Claude)
- ✅ Документувати архітектуру та інструкції

**Додатково (для більш високої оцінки):**
- ✅ Реалізувати alerting на основі AI аналізу
- ✅ Anomaly detection з Machine Learning
- ✅ Custom MCP tools для різних типів аналізу
- ✅ Integration з Slack/Discord для notifications
- ✅ Performance optimization recommendations

### 2.2 Архітектура

```
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                        │
├─────────────────────────────────────────────────────────────┤
│ • app-1 (Python Flask) → generates logs                     │
│ • app-2 (Node.js Express) → generates logs                  │
│ • Test Generator (load testing + error simulation)          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    ELK Stack (Docker)                       │
├─────────────────────────────────────────────────────────────┤
│ • Logstash (Collection & Parsing)                           │
│   └── Pipelines for different log formats                   │
│ • Elasticsearch (Storage & Indexing)                        │
│   └── Indices: logs-app1-*, logs-app2-*                     │
│ • Kibana (Visualization)                                    │
│   └── Dashboards: Performance, Errors, Traffic              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              MCP Server (AI Analysis Layer) 🆕              │
├─────────────────────────────────────────────────────────────┤
│ • MCP Tools:                                                │
│   - get_latest_logs(app, count)                            │
│   - search_logs(query, filters)                            │
│   - analyze_errors(timeframe)                              │
│   - detect_anomalies(metric)                               │
│   - generate_report(type)                                  │
│                                                             │
│ • Claude AI Integration:                                    │
│   - Anomaly Detection                                       │
│   - Root Cause Analysis                                     │
│   - Performance Recommendations                            │
│   - Trend Analysis                                         │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Структура проекту

```
stt-elk-mcp-logging/
├── README.md                        # Main documentation
├── docker-compose.yml               # ELK + Apps stack
│
├── apps/                            # Sample applications
│   ├── app1-python/
│   │   ├── app.py                   # Flask app
│   │   ├── logger_config.py          # Logging setup
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── app2-nodejs/
│   │   ├── server.js                # Express app
│   │   ├── logger.js                # Winston logger
│   │   ├── Dockerfile
│   │   └── package.json
│   │
│   └── load-generator/
│       ├── generate_traffic.py       # Load testing
│       └── error_simulator.py        # Inject errors
│
├── elk-config/                      # ELK configuration
│   ├── logstash/
│   │   ├── pipelines/
│   │   │   ├── app1-python.conf      # Python app pipeline
│   │   │   ├── app2-nodejs.conf      # Node.js app pipeline
│   │   │   └── common-filters.conf   # Shared filters
│   │   └── logstash.yml
│   │
│   ├── elasticsearch/
│   │   ├── elasticsearch.yml
│   │   └── index-templates/
│   │       ├── logs-app1-template.json
│   │       └── logs-app2-template.json
│   │
│   └── kibana/
│       ├── kibana.yml
│       └── dashboards/
│           ├── dashboard-performance.json
│           ├── dashboard-errors.json
│           └── dashboard-traffic.json
│
├── mcp-server/                      # MCP Server (AI Integration)
│   ├── server.py                    # MCP server implementation
│   ├── tools/
│   │   ├── elasticsearch_tools.py    # ES query tools
│   │   ├── analysis_tools.py         # Analysis functions
│   │   ├── anomaly_detection.py      # ML-based detection
│   │   └── report_generator.py       # Report generation
│   ├── claude_client.py              # Claude API integration
│   ├── requirements.txt
│   └── Dockerfile
│
├── tests/                           # Testing
│   ├── test_logstash_pipelines.py
│   ├── test_mcp_tools.py
│   └── test_kibana_dashboards.py
│
├── docs/                            # Documentation
│   ├── architecture.md              # System design
│   ├── elk-setup.md                 # ELK installation guide
│   ├── mcp-integration.md           # MCP setup + examples
│   ├── ai-analysis-guide.md         # Using Claude for analysis
│   └── troubleshooting.md
│
└── scripts/
    ├── start-stack.sh               # Start all services
    ├── generate-sample-logs.py       # Create test data
    └── cleanup.sh                   # Remove volumes
```

---

## 3. КОМПОНЕНТИ ЗАВДАННЯ

### 3.1 ELK Stack (Traditional Part)

#### Elasticsearch
- **Конфігурація:** 3-node cluster (або single node для dev)
- **Indexes:** Temporal indexes (logs-app1-YYYY.MM.DD)
- **Mapping:** Custom field types для структурованих логів

#### Logstash
- **Input:** File beats або TCP input від додатків
- **Filters:**
  - Grok patterns для парсингу
  - Mutate for enrichment (додавання service name, etc.)
  - Conditional processing
- **Output:** Elasticsearch

#### Kibana
- **Visualizations:**
  - Time series для traffic
  - Error rate trends
  - Log level distribution
  - Response time analysis
- **Dashboards:**
  - Real-time monitoring
  - Historical analysis
  - Per-service views

### 3.2 MCP Server + AI Analysis (NEW PART) 🆕

#### MCP Tools (Custom)
```python
class LogAnalysisMCPServer:
    # Tool 1: Get latest logs
    def get_latest_logs(app: str, limit: int = 100) -> List[Log]

    # Tool 2: Search with filters
    def search_logs(query: str, filters: Dict) -> List[Log]

    # Tool 3: Error analysis
    def analyze_errors(app: str, timeframe: str) -> ErrorReport

    # Tool 4: Anomaly detection
    def detect_anomalies(metric: str, sensitivity: float) -> List[Anomaly]

    # Tool 5: Performance analysis
    def analyze_performance(app: str, timeframe: str) -> PerformanceReport

    # Tool 6: Generate insights
    def generate_ai_insights(logs: List[Log]) -> str  # Claude generates

    # Tool 7: RCA (Root Cause Analysis)
    def perform_rca(incident: Incident) -> RCAReport
```

#### Claude AI Integration
```python
# Example workflow
1. User asks: "Why are we getting 500 errors?"
2. Claude uses MCP tools:
   - search_logs("status:500", {"timeframe": "1h"})
   - analyze_errors("app1", "1h")
   - detect_anomalies("error_rate", 2.0)
3. Claude synthesizes analysis and generates:
   - Root cause hypothesis
   - Affected services
   - Recommended actions
   - Links to relevant logs
```

---

## 4. ЛАБОРАТОРНІ ВПРАВИ

### Вправа 1: ELK Setup (Неділя 1)
- [ ] Docker Compose stack setup
- [ ] Elasticsearch cluster initialization
- [ ] Logstash pipeline configuration
- [ ] Kibana dashboard creation

### Вправа 2: Log Generation (Неділя 1-2)
- [ ] Implement Python Flask app with structured logging
- [ ] Implement Node.js Express app with Winston logger
- [ ] Create load generator for realistic traffic
- [ ] Inject errors to create interesting logs

### Вправа 3: Logstash Pipelines (Неділя 2)
- [ ] Parse Python JSON logs
- [ ] Parse Node.js structured logs
- [ ] Enrich with metadata (environment, version)
- [ ] Create custom fields for analysis

### Вправа 4: Kibana Dashboards (Неділя 2)
- [ ] Performance Dashboard (response times, throughput)
- [ ] Error Dashboard (error rates, error types)
- [ ] Traffic Dashboard (requests per service)

### Вправа 5: MCP Server Setup (Неділя 3)
- [ ] Implement MCP server in Python
- [ ] Connect to Elasticsearch
- [ ] Create MCP tools for log queries
- [ ] Test tool execution

### Вправа 6: Claude AI Integration (Неділя 3-4)
- [ ] Set up Claude API integration
- [ ] Implement prompt templates for analysis
- [ ] Test end-to-end: logs → MCP → Claude → insights
- [ ] Create example analysis workflows

### Вправа 7: Anomaly Detection (Неділя 4)
- [ ] Implement statistical anomaly detection
- [ ] Create baseline metrics
- [ ] Generate alerts for outliers
- [ ] Integrate with Claude for smart alerting

---

## 5. ОЧІКУВАНІ РЕЗУЛЬТАТИ

### Dashboard 1: Performance Overview
```
Metrics:
- Average response time (by service)
- P95 latency
- Throughput (requests/min)
- Error rate %
- CPU/Memory usage
```

### Dashboard 2: Error Analysis
```
Metrics:
- Error rate timeline
- Top error types
- Error distribution by service
- Stack traces (grouped)
- Error trends (hourly/daily)
```

### Dashboard 3: AI-Powered Insights
```
Features:
- Recent anomalies detected
- Potential issues identified by Claude
- Performance trends
- Recommended actions
- Links to detailed logs
```

### MCP Analysis Examples

**Example 1: Quick troubleshooting**
```
User: "Why is app2 slow?"
Claude analysis:
- Recent spike in response times detected
- Correlated with increase in database queries
- Recommendation: Check database indexes
- Links to slow query logs
```

**Example 2: Anomaly explanation**
```
User: "What's causing the error spike?"
Claude analysis:
- 500 errors increased 10x in last 30 mins
- Root cause: Out of memory in cache layer
- Affected users: ~5000
- Recommendation: Restart cache service
- Timeline: Issue started 14:23, fixed 14:45
```

**Example 3: Trend analysis**
```
User: "How is our system health?"
Claude analysis:
- Overall healthy with minor degradation
- Error rate normal (0.02%)
- Latency increasing slowly (trend: up 5% week-over-week)
- Recommendation: Monitor database growth
- Forecast: May hit limits in 2 weeks at current growth
```

---

## 6. ТЕХНІЧНІ ВИМОГИ

### Dependencies
- Docker & Docker Compose
- Python 3.9+
- Node.js 16+
- Elasticsearch 8.x
- Kibana 8.x
- Logstash 8.x
- Claude API key
- MCP SDK (Python)

### Ports
- Elasticsearch: 9200 (API), 9300 (cluster)
- Kibana: 5601
- Logstash: 5000 (input), 9600 (monitoring)
- App1 (Python): 5000
- App2 (Node.js): 3000
- MCP Server: 8000

### Storage
- Elasticsearch volume: ~10GB (for sample data)
- Log files: ~1GB

---

## 7. ОЦІНКА КРИТЕРІЇВ

| Критерій | Вага | Оцінка |
|----------|------|--------|
| ELK Stack deployment | 20% | ✅ All services running |
| Log parsing & enrichment | 20% | ✅ Correct field extraction |
| Kibana dashboards | 15% | ✅ 3+ useful dashboards |
| MCP Server implementation | 20% | ✅ All tools functional |
| Claude AI integration | 15% | ✅ Meaningful insights |
| Documentation | 10% | ✅ Clear setup guide |
| **Total** | **100%** | |

---

## 8. МАТЕРІАЛИ ДЛЯ DATASET

### Документація
- `elk-complete-guide.md` — Full ELK setup guide
- `logstash-pipeline-tutorial.md` — Pipeline configuration
- `kibana-dashboard-guide.md` — Dashboard creation
- `mcp-server-setup.md` — MCP server implementation
- `claude-integration-guide.md` — Claude API integration
- `log-analysis-patterns.md` — Common analysis patterns
- `anomaly-detection-guide.md` — ML-based detection

### Code Examples
- `example-logstash-pipeline.conf` — Working pipeline
- `example-python-logging.py` — Structured logging
- `example-nodejs-logging.js` — Winston logger setup
- `example-mcp-tools.py` — MCP tool templates
- `example-claude-prompts.md` — Prompt engineering
- `example-docker-compose.yml` — Full stack setup

### Templates
- `kibana-dashboard-template.json`
- `logstash-mapping-template.json`
- `elasticsearch-index-template.json`
- `mcp-server-template.py`

---

## 9. ПОСИЛАННЯ НА РЕСУРСИ

### Офіційна документація
- [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Kibana User Guide](https://www.elastic.co/guide/en/kibana/current/index.html)
- [Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)
- [MCP Specification](https://modelcontextprotocol.io/)
- [Claude API Documentation](https://docs.anthropic.com/)

### Tutorials & Guides
- [ELK Stack Tutorial](https://www.elastic.co/what-is/elk-stack)
- [Structured Logging Best Practices](https://www.kartar.net/2015/12/structured-logging/)
- [Anomaly Detection in ML](https://www.deepdive.ai/anomaly-detection)

---

## 10. ДОДАТКОВІ ВИКЛИКИ (BONUS)

- [ ] Real-time alerting (Slack/Discord integration)
- [ ] Machine Learning model training for better anomaly detection
- [ ] Custom visualization plugins for Kibana
- [ ] Integration with APM (Application Performance Monitoring)
- [ ] Multi-tenant log isolation
- [ ] Log retention & archival policies
- [ ] Performance optimization (sharding, caching)
- [ ] Compliance & security (encryption, access control)

---

## 11. МЕТАІНФОРМАЦІЯ

**Статус:** SPECIFICATION READY (готово до розробки)
**Складність:** Advanced (для студентів 2-3 року)
**Синергія:** Поєднує:
- Chapter 12: Metrics & Quality
- Chapter 11: Technical Foundations
- Chapter 13: Automation
- Chapter 15: AI Testing
- Modern DevOps practices

**Новизна:** 🆕 Перше завдання з MCP + Claude AI integration для QA/observability

**Потенціал:** Може розширитися у окремий advanced курс або enterprise workshop

---

**Документ готовий до інтеграції у HANDBOOK_STRUCTURE.md**
