
# Введение в BDD


![](https://habrastorage.org/r/w1560/getpro/habr/upload_files/da7/01e/a12/da701ea12d63543b9261ae649a4c3f51.png)

На протяжении истории люди придумывали различные подходы и приёмы, как разрабатывать более качественные и поддерживаемые приложения. В этой статье я бы хотел рассказать о такой методологии разработки, как **BDD (Behaviour Driven Development)**. Но прежде чем перейти непосредственно к гвоздю программы — небольшое вступление.

Думаю, большинство разработчиков согласятся с мыслью о том, что покрытый юнит-тестами код лучше, чем непокрытый. Действительно, тесты позволяют эффективно следить за работоспособностью кода, вовремя отлавливать нерабочие изменения. А ещё из наличия юнитов обычно следует то, что код разбит на логические модули и каждый класс/функция имеет одну зону ответственности (привет SOLID). Тот, кому доводилось писать тест на большую функцию с несколькими зонами ответственности знает, что тесты на такую функцию обречены быть хрупкими и падать при малейшем изменении. Это заставляет задуматься о том, чтобы не писать всё "в одной портянке", а писать гибкий код, поделённый на модули. С таким кодом, как правило, приятнее работать, т.к. приходится держать в уме меньше информации.

В какой-то момент люди сделали вывод, что раз код хороший если он тестируемый, тогда давайте мы сначала напишем тесты на этот код, а уже потом сам код. И так придумали методологию...

### Test Driven Development (TDD)

**Test Driven Development (TDD)** — это подход к разработке программного обеспечения, который ставит тестирование на первое место. В TDD разработчики сначала пишут тесты для новой функциональности, а затем пишут код, который позволит этим тестам пройти. Это отличается от традиционного подхода, когда тесты пишутся после кода, однако привносит свои преимущества:

* **Повышение качества кода:** Тесты обеспечивают быструю обратную связь о том, работает ли код так, как предполагалось.
* **Упрощение рефакторинга:** Тесты служат "сетью безопасности", позволяя разработчикам вносить изменения в код без страха сломать что-то.
* **Документация:** Тесты могут служить формой документации, показывая, как предполагается использование кода.

Программист при написании тестов по сути занимается проектированием и составлением требований к модулю, заранее продумывая что это будет за модуль и за что он будет отвечать.

![Подобно созданию чертежа перед постройкой дома, TDD вынуждает программиста лишний раз подумать о том, как будет выглядеть и использоваться его код](https://habrastorage.org/r/w1560/getpro/habr/upload_files/53c/ee3/74d/53cee374df5ff2c4ac5bc6008f2ac6e8.jpeg "Подобно созданию чертежа перед постройкой дома, TDD вынуждает программиста лишний раз подумать о том, как будет выглядеть и использоваться его код")

Подобно созданию чертежа перед постройкой дома, TDD вынуждает программиста лишний раз подумать о том, как будет выглядеть и использоваться его код

Конечно, за всё приходится платить, и TDD не является исключением:

* **Замедление процесса разработки:** Написание тестов занимает время, которое могло бы быть потрачено на написание нового кода.
* **Трудность написания хороших тестов:** Написание эффективных тестов — это навык, который требует практики и опыта.
* **Риск переосмысления:** Существует риск, что разработчики могут проводить слишком много времени, пытаясь заставить тесты пройти, вместо того чтобы думать о лучшем дизайне системы.

### Behavior Driven Development как развитие TDD

Людям хотелось использовать TDD подход не только в вопросах реализации того или иного функционала, но и для более широких вещей. Хотелось иметь достаточно ясные тесты, взглянув на которые у человека не составило бы труда понять, что умеет делать определённая часть приложения. Проблема в том, что классические тесты не всегда могут быть сразу понятными для человека, увидевшего ваше приложение в первый раз. Здесь и появляется BDD.

**Behavior Driven Development (BDD)** — это подход к разработке программного обеспечения, который вырос из TDD. В то время как TDD сосредоточен на тестировании отдельных модулей кода, BDD расширяет этот подход, сосредоточиваясь на поведении системы в целом.

При написании BDD тестов реализуются степы, или шаги — небольшие функции, которые выполняют одно определённое действие юзера. BDD использует естественный язык и конкретные примеры для описания ожидаемого поведения системы. Это помогает улучшить коммуникацию между разработчиками, тестировщиками и непрограммистами, такими как менеджеры проектов или стейкхолдеры.

#### Принципы BDD

BDD основывается на нескольких ключевых принципах:

1. **Описание поведения**: Вместо того чтобы сосредоточиваться на технических деталях реализации, BDD фокусируется на описании ожидаемого поведения системы с точки зрения пользователя или стейкхолдера. Это помогает убедиться, что разрабатываемые функции действительно соответствуют потребностям пользователей.
2. **Использование естественного языка**: BDD использует естественный язык для описания сценариев тестирования, что делает их понятными не только для разработчиков и тестировщиков, но и для менеджеров проектов, бизнес-аналитиков и других участников команды.
3. **Сотрудничество и коммуникация**: BDD подчеркивает важность сотрудничества и общения между всеми участниками команды. Это помогает обеспечить общее понимание целей и требований проекта.
4. **Примеры**: BDD использует конкретные примеры для описания ожидаемого поведения. Это помогает уточнить требования и обеспечивает ясность в отношении того, что должна делать система.

![Цикл BDD](https://habrastorage.org/r/w1560/getpro/habr/upload_files/1e7/29e/f09/1e729ef09951ef53e33ac3ec386bbf2a.png "Цикл BDD")

Цикл BDD

Как и любой подход, BDD имеет свои преимущества и недостатки.

**Плюсы**:

1. **Повышение качества коммуникации**: BDD использует естественный язык для описания ожидаемого поведения, что делает его понятным для всех участников команды, включая непрограммистов.
2. **Сосредоточение на бизнес-целях**: BDD помогает команде сосредоточиться на достижении конкретных бизнес-целей, а не просто на написании кода.
3. **Поддержка автоматизации тестирования**: BDD поддерживает автоматизацию тестирования, что позволяет быстро и эффективно проверять поведение системы.

**Минусы**:

1. **Сложность внедрения**: Внедрение BDD может потребовать значительных изменений в процессах разработки и тестирования, что может быть сложно для некоторых команд.
2. **Требуется обучение**: Для эффективного использования BDD команде может потребоваться обучение, особенно для понимания и написания сценариев на естественном языке.
3. **Риск неправильного понимания**: Если сценарии BDD написаны неправильно или нечетко, это может привести к неправильному пониманию требований или ожидаемого поведения системы.

При разработке BDD тестов можно использовать два подхода:

1. **Тест-кейсы и реализация степов на классическом ЯП**.   
   Сами тесты должны выглядеть максимально понятно и не содержать сложной логики. Условный BDD-тест на Python может выглядеть так:

   ```c
   class FeatureCalculator:
       """
       As a user
       I want to perform some math ops
       """

       def test_one_plus_one(self):
           """
           I can successfully add one to one
           """
           # Given
           self.working_calculator()
           # When
           self.i_add(1, 1)
           # Then
           self.result_is(2)

       def test_one_plus_one_broken_calculator(self):
           """
           I try to add one to one using broken calculator
           """
           # Given
           self.broken_calculator()
           # When
           self.i_add(1, 1)
           # Then
           self.result_is(None)

       def working_calculator(self):
           ...

       def broken_calculator(self):
           ...

       def i_add(self, x, y):
           ...

       def result_is(self, x):
           ...

      ```
2. **Тест-кейсы на Gherkin, реализация степов на классическом ЯП.**   
   [Gherkin](https://docs.cucumber.io/docs/gherkin/reference/) — это язык, созданный специально для описания поведения систем. Содержит небольшое количество ключевых слов, которое тем не менее является достаточным для составления тестовых сценариев. Тот же самый тест, но на Gherkin:

   ```c
   Feature: Calculator
     As a user
     I want to perform some math ops

     Scenario: I can successfully add one to one
       Given working calculator
        When I add 1 to 1
        Then result is 2

     Scenario: I try to add one to one using broken calculator
       Given broken calculator
        When I add 1 to 1
        Then result is None

      ```

### Практическая часть: Примеры BDD тестов с использованием библиотеки python-behave

Для практики давайте покроем BDD тестами некоторое приложение. На SwaggerHub выложен в открытом доступе [Swagger Petstore](https://petstore.swagger.io/#/) — REST API для управления неким "магазином домашних питомцев". Попробуем покрыть тестами endpoint `POST /pet`, отвечающий за добавление нового питомца в магазин.

Писать тесты я буду с использованием Gherkin. Для реализации таких тестов я выбрал Python 3.10 + фреймворк `python-behave`. Установить его можно через pip:

`pip install behave`

Впрочем, BDD фреймворков существует много для таких языков как Java, C#, Go, JavaScript и другие.

Запуск BDD тестов происходит через консоль командой `behave`, либо через плагины для вашего любимого инструмента разработки (например в PyCharm Professional поддержка BDD есть из коробки).

#### Примеры BDD тестов

Создадим новый feature-файл:

**features/pet.feature**

```c
Feature: Everything about your Pets
  As user I want to add, update, and delete pets in the pet store

  # здесь будут располагаться тесты
  # Scenario: ...

```

Для первого запуска напишем простой тест, который будет посылать POST запрос на API и ожидать, что получит в ответ `200`.

**features/pet.feature**

```c
  Scenario: I successfully create new empty pet
    When I make POST request to "/pet" with body
    Then Response is 200

```

Но этот тест не запустится прямо сейчас, потому что мы не реализовали поведение для шагов `I make POST request to "/pet" with body` и `Response is 200`:

```c
Feature: Everything about your Pets # features/pet.feature:1
  As user I want to add, update, and delete pets in the pet store
  Scenario: I successfully create new empty pet  # features/pet.feature:4
    When I make POST request to "/pet" with body # None
    Then Response is 200                         # None

Failing scenarios:
  features/pet.feature:4  I successfully create new empty pet

0 features passed, 1 failed, 0 skipped
0 scenarios passed, 1 failed, 0 skipped
0 steps passed, 0 failed, 0 skipped, 2 undefined
Took 0m0.000s

You can implement step definitions for undefined steps with these snippets:

@when(u'I make POST request to "/pet" with body')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I make POST request to "/pet" with body')

@then(u'Response is 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Response is 200')

```

Давайте это исправим:

**features/steps/pet.py**

```c
import json

import requests
from behave import step

ROOT_URL = r"https://petstore.swagger.io/v2"

@step('I make POST request to "{path}" with body')
def make_post_request_step(context, path):
    body = json.loads(context.text or "{}")
    url = ROOT_URL + path
    context.response = requests.post(url, json=body)

@step("Response is {status_code:d}")
def assert_response_step(context, status_code):
    assert (
        context.response.status_code == status_code,
        f"Expected {status_code}, got {context.response.status_code}"
    )

```

Попробуем запустить ещё раз:

```c
Feature: Everything about your Pets # features/pet.feature:1
  As user I want to add, update, and delete pets in the pet store
  Scenario: I successfully create new empty pet  # features/pet.feature:4
    When I make POST request to "/pet" with body # features/steps/pet.py:9
    Then Response is 200                         # features/steps/pet.py:17

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
2 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.927s

```

Удостоверимся, что тест работает, немного поломав его. Пусть мы будем ожидать ответ `300` вместо `200`:

```c
Feature: Everything about your Pets # features/pet.feature:1
  As user I want to add, update, and delete pets in the pet store
  Scenario: I successfully create new empty pet  # features/pet.feature:4
    When I make POST request to "/pet" with body # features/steps/pet.py:9
    Then Response is 300                         # features/steps/pet.py:17
      Assertion Failed: Expected 300, got 200

Failing scenarios:
  features/pet.feature:4  I successfully create new empty pet

0 features passed, 1 failed, 0 skipped
0 scenarios passed, 1 failed, 0 skipped
1 step passed, 1 failed, 0 skipped, 0 undefined
Took 0m1.026s

```

Замечательно! Теперь при помощи этих шагов можно написать и негативные сценарии:

**features/pet.feature**

```c
  Scenario: I get an error if I try to create a pet with invalid category id
    When I make POST request to "/pet" with body
      """
      {
        "category": {"id": "zero", "name": "cats"}
      }
      """
    Then Response is 500

  Scenario: I get an error if I try to create a pet with invalid tag id
    When I make POST request to "/pet" with body
      """      {
        "tags": {"id": "zero", "name": "puffy"}
      }
      """
    Then Response is 500

```

Всё это здорово, но довольно-таки простовато. Всё же мы бы хотели как-то проверять сам контент возвращаемого JSON-а. Давайте добавим новый шаг, в котором мы бы могли сравнивать контент JSON-а с описанным в тесте.

**feature/steps/pet.py**

```c
def has_json_response(context) -> bool:
    try:
        context.response.json()
        return True
    except ValueError or AttributeError:
        return False

@step("Response contains json with items")
def assert_response_contains_json(context):
    assert (
        has_json_response(context),
        f"Expected json, but got {context.response.text}"
    )
    actual_values = context.response.json()
    expected_values = json.loads(context.text)
    for field in expected_values:
        expected_value = expected_values[field]
        actual_value = actual_values[field]
        match expected_value:
            case "<{any_int}>":
                assert (
                    isinstance(actual_value, int),
                    f'Expected "{field}" is a number value, got {actual_value}'
                )
            case _:
                assert (
                    expected_value == actual_value,
                    f'Expected "{field}" equals {expected_value}, got {actual_value}'
                )

```

Рассмотрев внимательнее реализацию этого степа, можно заметить, что он может делать две вещи:

* проверка на равенство значений, если в качестве ожидаемого значения указать число
* проверка на принадлежность значения множеству целых чисел, если в качестве ожидаемого значения указать строку `<{any_int}>`

Такое поведение пригодится нам, потому что зачастую мы не можем знать наверняка, какое значение имеет то или иное поле, но нам достаточно проверить, что в таком поле содержится любое число.

Обновим первый тест:

**features/pet.feature**

```c
  Scenario: I successfully create new empty pet
    When I make POST request to "/pet" with body
    Then Response is 200
     And Response contains json with items
      """
      {
        "id": "<{any_int}>",
        "tags": [],
        "photoUrls": []
      }
      """

```

Напоследок давайте попробуем написать параметризованный сценарий, в котором мы создадим нового питомца с заданными полями:

**features/pet.feature**

```c
  Scenario Outline: I successfully create new pet with specified name, category, status, tags and photo
    When I make POST request to "/pet" with body
      """
      {
        "name": "Barsik",
        "category": {"name": "cats"},
        "status": "<category>",
        "tags": [
          {"name": "puffy"},
          {"name": "young"}
        ]
      }
      """
    Then Response is 200
     And Response contains json with items
      """
      {
        "id": "<{any_int}>",
        "name": "Barsik",
        "category": {"id": 0, "name": "cats"},
        "status": "<category>",
        "tags": [
          {"id": 0, "name": "puffy"},
          {"id": 0, "name": "young"}
        ],
        "photoUrls": []
      }
      """

    Examples:
      | category  |
      | available |
      | pending   |
      | sold      |

```

Полностью проект доступен по ссылке: [github.com/rmksrv/swaggerhub-petstore-bdd](https://github.com/rmksrv/swaggerhub-petstore-bdd)

### Заключение

Целью этой статьи было познакомить читателя с BDD методологией, и, поскольку это было знакомство, то мы прошлись только по верхам. Тем не менее этого вполне достаточно, чтобы использовать её в своих проектах. Основное преимущество данного подхода заключается в возможности написания тестов на естественном языке, что делает понятным требуемое поведение системы. При вдумчивом подходе, в конце концов, можно получить такие тесты, которые были бы достаточно ясны и читабельны, чтобы их скинуть вашему бизнес-аналитику вместо документации. А в некоторых случаях и бизнес-аналитик сможет сам накидать пару тестовых сценариев.

Материал был написан в феврале 2024-го года на основании опыта, полученного во время работы в ООО «Аурига».

Надеюсь, что статья была интересной и благодарю за внимание!

Теги:

* [тестирование по](/ru/search/?target_type=posts&order=relevance&q=[%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%D0%BF%D0%BE])
* [bdd](/ru/search/?target_type=posts&order=relevance&q=[bdd])
* [tdd](/ru/search/?target_type=posts&order=relevance&q=[tdd])

Хабы:

* [Блог компании Аурига](/ru/companies/auriga/articles/)
* [Тестирование IT-систем](/ru/hubs/it_testing/)
* [TDD](/ru/hubs/tdd/)
