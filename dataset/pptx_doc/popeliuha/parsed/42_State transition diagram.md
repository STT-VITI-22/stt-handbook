# 42_State transition diagram

# State transition diagram

## Діаграма переходу станів

* Діаграма переходу станів показує початковий і кінцевий стан системи, а також описує переходи між станами.
* Діаграма переходу станів показує лише валідні переходи.
* Діаграма складається з пар переходів між двома станами.
* Якщо переходу між двома станами немає, то перехід вважається НЕвалідним.

```mermaid
stateDiagram-v2
    [*] --> S1
    S1 --> S2: A
    S2 --> S3: B
    S3 --> S2: C
    S2 --> S1: D
```

## Діаграма переходу станів

```mermaid
stateDiagram-v2
    direction LR
    Лід --> Вода: A
    Вода --> Лід: D
    Вода --> Пар: B
    Пар --> Вода: C
    Лід --> Пар
    Пар --> Лід
```

| Test Case ID | TC01 | TC02 | TC03 | TC04 |
| :--- | :--- | :--- | :--- | :--- |
| Початковий стан | Лід | Вода | Вода | Пар |
| Перехід | A | D | B | C |
| Фінальний стан | Вода | Лід | Пар | Вода |

Ґрунтуючись на діаграмі переходу станів вмикача, який тест невалідний?

* Вимкнено-> ввімкнено
* Ввімкнено -> вимкнено
* Помилка -> ввімкнено
* Ввімкнено -> помилка

```mermaid
stateDiagram-v2
    [*] --> S1
    S1: Вимкнено
    S2: Ввімкнено
    S3: Помилка

    S1 --> S2
    S2 --> S1
    S2 --> S3
    S3 --> S3
```

Грунтуючись на діаграмі переходу станів вмикача, який тест невалідний?

* Вимкнено -> ввімкнено
* Ввімкнено -> вимкнено
* **Помилка -> ввімкнено**
* Ввімкнено -> помилка

```mermaid
stateDiagram-v2
    [*] --> Вимкнено: S1
    Вимкнено --> Ввімкнено: S2
    Ввімкнено --> Вимкнено: S2
    Ввімкнено --> Помилка: S3
    Помилка --> Помилка: S3
```

Грунтуючись на діаграмі переходу станів вмикача, який тест невалідний?

* Вимкнено-> ввімкнено
* Ввімкнено -> вимкнено
* **Помилка -> ввімкнено**
* Ввімкнено -> помилка

```mermaid
stateDiagram-v2
    direction TB
    
    S1: Вимкнено
    S2: Ввімкнено
    S3: Помилка

    [*] --> S1
    S1 --> S2
    S2 --> S1
    S2 --> S3
    S3 --> S3
```

## Приклад з відкритого доступу #1

![Діаграма переходів станів життєвого циклу](images/42_State%20transition%20diagram/page_7_img_1.jpeg)

```mermaid
stateDiagram-v2
    [*] --> Start
    Start --> Child: Born
    Child --> End: Dies
    Child --> Adult: Turns 18
    Adult --> End: Dies
    Adult --> Geriatric: Turns 76
    Geriatric --> End: Dies
```

## Приклад з відкритого доступу #2

![State Transition Diagram for ATM System](images/42_State%20transition%20diagram/page_8_img_1.jpeg)

```mermaid
stateDiagram-v2
    [*] --> ReadingCard
    ReadingCard --> EjectingCard: Invalid Card
    ReadingCard --> ReadingPin: Card read successfully
    ReadingPin --> EjectingCard: Invalid Pin
    ReadingPin --> ChooosingTransaction: Getting valid pin
    ChooosingTransaction --> EjectingCard: Cancel transaction
    ChooosingTransaction --> PerformingTransaction: Transaction choosen
    PerformingTransaction --> EjectingCard: Finished transaction
    EjectingCard --> [*]
    PerformingTransaction --> ChooosingTransaction: Another transaction
```

## Приклад з відкритого доступу #3

![Діаграма станів (State Transition Diagram)](images/42_State%20transition%20diagram/page_9_img_1.jpeg)

```mermaid
stateDiagram-v2
    [*] --> Start
    Start --> ListShow: Search to add friend
    
    ListShow --> FriendRejected: Reject friend
    ListShow --> FriendAdded: Accept friend
    ListShow --> FriendRejected: Again add
    
    state decision <<choice>>
    ListShow --> decision: Add friend
    
    decision --> UserBlocked: Block user
    decision --> End: Close
    decision --> FriendRejected: Reject friend
    decision --> FriendAdded: Accept friend
    
    UserBlocked --> End: close
    FriendRejected --> End: close
    FriendAdded --> End: close
```

[https://app.diagrams.net/](https://app.diagrams.net/)

