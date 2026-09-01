# 45_Decision coverage

# Decision coverage

## Покриття умов

# Вступ до технік білого ящика

* Statement testing (тестування операторів) тестує оператори в даному фрагменті коду
* Decision testing (тестування умов) тестує умови в даному фрагменті коду
* Тестування умов ще відоме як Branch testing
* Тестування умов сильніше, ніж тестування операторів.
* 100% покриття умов гарантує 100% покриття операторів, але не навпаки.

# Пояснювальна бригада - блок-схеми

```text
Read A
Read B
If A>B then
    Print “А більше”
Else
    Print “В більше”
End if
```

Шлях - це проходження по коду, починаючи з точки старт і закінчуючи точкою кінець.

```mermaid
graph TD
    start([start]) --> AB[A, B]
    AB --> Cond{A>B}
    Cond -- True --> A[A]
    Cond -- False --> B[B]
    A --> EndIf[End if]
    B --> EndIf
    EndIf --> EndNode([end])
```

# Пояснювальна бригада - блок-схеми

```text
Read A
Read B
If A>B then
    Print “А більше”
Else
    Print “В більше”
End if
```

Скільки потрібно створити мінімум тест кейсів на 100% decision покриття?

```mermaid
graph TD
    start([start]) --> AB[A, B]
    AB --> Cond{A>B}
    Cond -- True --> A[A]
    Cond -- False --> B[B]
    A --> EndIf[End if]
    B --> EndIf
    EndIf --> End([end])
```

* **Decision coverage** = мін. к-ть шляхів, потрібна для покриття всіх branches
* **Decision coverage** = 2

## Приклад #1

Чекати, щоб вставили картку

IF карта валідна THEN
  показати "Введіть PIN-код"
  IF PIN валідний THEN
    вибрати транзакцію
  ELSE
    показати "PIN невалідний"
ELSE
  відхилити карту

```mermaid
graph TD
    A[Чекати] --> B{Валідна картка?}
    B -->|Так| C["Показати Введіть..."]
    B -->|Ні| D[Відхилити карту]
    D --> G
    C --> E{Валідний PIN?}
    E -->|Так| F[Обрати транзакц...]
    E -->|Ні| H["Показати PIN нева..."]
    F --> G([Кінець])
    H --> G
```

## Приклад #1

**TIP: Decision coverage = 1 + к-ть IF (у statement - else)**

Чекати, щоб вставили картку
- IF карта валідна THEN
    - показати “Введіть PIN-код”
    - IF PIN валідний THEN
        - вибрати транзакцію
    - ELSE
        - показати “PIN невалідний”
- ELSE
    - відхилити карту

**Decision coverage = 3**

```mermaid
graph TD
    A[Чекати] --> B{Валідна картка?}
    B -->|Так| C["Показати Введіть..."]
    B -->|Ні| D[Відхилити карту]
    C --> E{Валідний PIN?}
    E -->|Так| F[Обрати транзакц...]
    E -->|Ні| G["Показати PIN нева..."]
    D --> H[Кінець]
    G --> H
    F --> H
```

## Приклад #2

```text
Read A

IF A > 0 THEN
    IF A = 21 THEN
        Print “Key”
    ENDIF
ENDIF
```

**Decision coverage = 3**

```mermaid
graph TD
    Start([Read]) --> Cond1{A > 0}
    Cond1 -->|True| Cond2{A = 21}
    Cond1 -->|False| End([End])
    Cond2 -->|True| Print[Print]
    Cond2 -->|False| End
    Print --> End
```

# Приклад #3

Decision coverage = 4

Read A
Read B
IF A > 0 THEN
    IF B = 0 THEN
        Print “No values”
    ELSE
        Print B
    IF A > 21 THEN
        Print A
    ENDIF
    ENDIF
ENDIF

```mermaid
graph TD
    Read --> CondA["A > 0"]
    CondA -->|True| CondB["B = 0"]
    CondA -->|False| End
    
    CondB -->|True| Print1["Print"]
    CondB -->|False| Print2["Print"]
    
    Print1 --> CondA21["A > 21"]
    CondA21 -->|True| Print3["Print"]
    CondA21 -->|False| End
    
    Print2 --> End
    Print3 --> End
    
    subgraph Legend
    end
```

## Приклад #4

Decision coverage = 2

```text
Read A
Read B
IF A < 0 THEN
    Print “A negative”
ELSE
    Print “A positive”
ENDIF
IF B < 0 THEN
    Print “B negative”
ELSE
Print “B positive”
ENDIF
```

```mermaid
graph TD
    Read --> Cond1{A < 0}
    Cond1 -- True --> PrintA1[Print]
    Cond1 -- False --> PrintA2[Print]
    PrintA1 --> Join1[Print]
    PrintA2 --> Join1
    Join1 --> Cond2{B < 0}
    Cond2 -- True --> PrintB1[Print]
    Cond2 -- False --> PrintB2[Print]
    PrintB1 --> Join2[Print]
    PrintB2 --> Join2
    Join2 --> End[End]
```

> **TIP:** Завжди, незалежно від ELSE або IF Decision покриття = 2

## Приклад #5

Для цього фрагмента коду було проведено такі шляхи/тести. Яке decision покриття досягнуто?

* Тест 1 - A, B, C
* Тест 2 - A, B, D, G, H

Decision покриття = кількість branches виконано / загальна кількість branches

1. 50%
2. **62%** (5 із 8 branches перевірено)
3. 75%
4. 100%

```mermaid
graph TD
    A --> B
    B --> C
    B --> D
    D --> F
    D --> G
    F --> G
    G --> H
    G --> I
```

