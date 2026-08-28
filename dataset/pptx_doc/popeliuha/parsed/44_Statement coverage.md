# 44_Statement coverage

# Statement coverage

## Покриття операторів

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

## Пояснювальна бригада - блок-схеми

```text
Read A
Read B
If A>B then
    Print “А більше”
Else
    Print “В більше”
End if
```

Скільки потрібно створити мінімум тест кейсів на 100% statement покриття?

```mermaid
graph TD
    start([start]) --> AB[A, B]
    AB --> Cond{A>B}
    Cond -->|True| A[A]
    Cond -->|False| B[B]
    A --> EndIf[End if]
    B --> EndIf
    EndIf --> EndNode([end])
    
    %% Пояснення поруч
    classDef comment fill:none,stroke:none;
```

* **Statement coverage** = мін. к-ть шляхів, потрібна для покриття всіх statements
* **Statement coverage** = 2

## Приклад #1

> **TIP:** Statement coverage = 1 + к-ть ELSE

* Чекати, щоб вставили картку
* IF карта валідна THEN
  * показати “Введіть PIN-код”
  * IF PIN валідний THEN
    * вибрати транзакцію
  * ELSE
    * показати “PIN невалідний”
* ELSE
  * відхилити карту

**Statement coverage = 3**

```mermaid
graph TD
    A[Чекати] --> B{Валідна картка?}
    B -->|Так| C[Показати 'Введіть...']
    B -->|Ні| D[Відхилити карту]
    C --> E{Валідний PIN?}
    E -->|Так| F[Обрати транзакц...]
    E -->|Ні| G[Показати 'PIN нева...]
    D --> H[Кінець]
    F --> H
    G --> H
```

## Приклад #2

```text
Read A

IF A > 0 THEN
    IF A = 21 THEN
        Print “Key”
    ENDIF
ENDIF

Statement coverage = 1
```

```mermaid
graph TD
    Read([Read]) --> Condition1{A > 0}
    Condition1 -->|Так| Condition2{A = 21}
    Condition1 -->|Ні| End([End])
    Condition2 -->|Так| Print[Print]
    Condition2 -->|Ні| End
    Print --> End
```

# Приклад #3

Statement coverage = 2

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
    Read --> Cond1{A > 0}
    Cond1 -->|True| Cond2{B > 0}
    Cond1 -->|False| End
    Cond2 -->|True| Print1[Print]
    Cond2 -->|False| Print2[Print]
    Print1 --> Cond3{A > 21}
    Cond3 -->|True| Print3[Print]
    Cond3 -->|False| End
    Print2 --> End
    Print3 --> End
```

## Приклад #4

Statement coverage = 2

```text
Read A
Read B

IF A < 0 THEN
    Print "A negative"
ELSE
    Print "A positive"
ENDIF

IF B < 0 THEN
    Print "B negative"
ELSE
    Print "B positive"
ENDIF
```

```mermaid
graph TD
    Read["Read"] --> CondA{"A < 0"}
    CondA -->|True| PrintNeg["Print"]
    CondA -->|False| PrintPos["Print"]
    PrintNeg --> Merge1((" "))
    PrintPos --> Merge1
    Merge1 --> CondB{"B < 0"}
    CondB -->|True| PrintB1["Print"]
    CondB -->|False| PrintB2["Print"]
    PrintB1 --> Merge2((" "))
    PrintB2 --> Merge2
    Merge2 --> End["End"]
```

* **TIP: Якщо є ELSE Statement покриття = 2**
* **Якщо немає ELSE Statement покриття = 1**

## Приклад #5

Для цього фрагмента коду було проведено такі шляхи/тести. Яке statement покриття досягнуто?

* Тест 1 - A, B, C
* Тест 2 - A, B, D, G, H

1. 50%
2. 75%
3. 90%
4. 100%

Statement покриття = кількість тверджень виконано / загальна кількість тверджень

6 із 8 тверджень перевірено

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

