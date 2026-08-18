# Тестирование WebSocket на клиентах

**Source:** https://vladislaveremeev.gitbook.io/qa_bible/seti-i-okolo-nikh/socket-websocket/testirovanie-websocket-na-klientakh

---

# Тестирование WebSocket на клиентах

Для тестирования всех фич работающих через сеть на клиентах (особенно мобильных) необходимо использовать снифферы трафика, такие как Charles, Fiddler, Proxyman и др. Они умеют перехватывать запросы, позволяют изменять их и настраивать автоматическую замену различных параметров согласно правилам. Однако, ситуация становится сложнее, когда речь доходит до тестирования WebSocket на тех же клиентах (в том числе web).

Есть множество инструментов с помощью, которых можно протеcтировать сам WebSocket, тот же Postman может выступать в роли клиента. Но, когда нам нужно протестировать как клиент реагирует на различные сообщения в нём, то возможности популярных снифферов сильно ограничены позволяют лишь просматривать сообщения в WebSocket c различным качеством удобства.

Если на проекте у вас есть инструмент со стороны бэкенда, способный отправлять собственные сообщения в веб-сокет или менять отравляемые и принимаемые сообщения со стороны, то возможно этого будет достаточно для проверки различных кейсов на клиентах. Таких как тестирование кастомных ответов от сервера, эмулирования ошибок. Когда бекенд не готов или на проде воспроизвести ситуацию трудно, а протестировать как будет вести клиент себя в этой ситуации нужно.

Если такого инструмента нет, то придётся прибегнуть к альтернативным решениям, способным уже не только показывать, но и перехватывать и изменять сообщения отправляемые в WebSocket.

Ниже рассмотрим два решения, которые позволят покрыть большинство кейсов, связанных с WebSocket.

* [Burp Suit](#burp-suit)
* [ZAP proxy](#id-instrumentytestirovaniyawebsocketnaklientakh-zapproxy.1)

| Burp Suite                                                                                                                                                                                                                                                  | ZAP Proxy                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://vladislaveremeev.gitbook.io/files/abPs6IHbVtRHiablDGtK" alt="" data-size="original">                                                                                                                                                                                         | <img src="https://vladislaveremeev.gitbook.io/files/Uz9DZRS5ZmDeFpFvSNGm" alt="" data-size="original">                                                                                                                                                                      |
| <p>Бесплатной версии хватит для выполнения основных задач. Не показывает Ping/Pong сообщения (или не получилось найти как включить)</p><p><a href="https://portswigger.net/burp/communitydownload"><https://portswigger.net/burp/communitydownload></a></p> | <p>Опенсурсное приложение, местами удобнее Burp при работе с ws, хотя есть и свои минусы. Плюс больше возможностей.</p><p>Скачать можно на сайте <a href="https://www.zaproxy.org/download/"><https://www.zaproxy.org/download/></a></p> |

## Burp Suit

***

При запуске нас просят выбрать проект.

В бесплатной версии можно работать только с временным проектом, однако для работы с WebSocket этого достаточно, все настройки можно экспортировать в файл конфигурации и применить на следующем экране.

### **Proxy**

Третий экран уже будет окно самого Burp, открываем сразу вкладку **Proxy**:

<div align="center"><figure><img src="https://vladislaveremeev.gitbook.io/files/jH3JvBcX187tlBjlQImY" alt="" width="375"><figcaption></figcaption></figure></div>

Здесь будет 5 вкладок/кнопок.

* **Intercept** – по сути тоже что брейкпоинты, при включении будет перехватывать все запросы соответствующие правилам заданным в настройках (об этом ниже).
* **HTTP history** – история HTTP запросов.
* **WebSockets history** – история сообщений внутри всех Websocket соединений. У каждого соединения задается в рамках сессии свой id – число, чтобы можно было их отличать.
* **Match and Replace** – можно быстро включать и отключать правила автозамены для запросов HTTP и сообщений в WebSocket. Дублирует тоже самое из настроек.
* **Proxy Setting** – настройки прокси.

### **Настройки – Proxy Settings** <a href="#id-instrumentytestirovaniyawebsocketnaklientakh-nastroiki-proxysettings" id="id-instrumentytestirovaniyawebsocketnaklientakh-nastroiki-proxysettings"></a>

Начать надо с настроек.

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/AWX409CuZk27PyZHS8wD" alt=""><figcaption></figcaption></figure></div>

Если проксируем мобильные клиенты, то надо разрешить все входящие соединения, для этого выбираем единственную строчку в **Proxy listeners** и жмём edit. Там прописываем свой порт и меняем **Bind to address** на **All interfaces**

<div align="left" data-full-width="false"><figure><img src="https://vladislaveremeev.gitbook.io/files/8wHp4Ct5aNzWgb5ki4Hw" alt="" width="563"><figcaption></figcaption></figure></div>

Экспортируем сертификат

* нажимаем **import / export CA certificate** внизу блока **Proxy listeners;**
* там выбираем **Certificate in DER format;**
* **Select file** и тут надо вручную ввести любое название и расширение .der
* Устанавливаем сертификат на смартфон или на компьютер (смотря где собираетесь смотреть), аналогично как это делали с другими снифферами.

#### **Request interception rules**

Здесь задаём правила для перехвата (брейкпоинтов). Burp автоматически перехватывает всё, что подходит условиям. Так как нам надо перехватывать только сообщения из вебсокета добавляем сюда правило **operator** – AND, **match type** – URL, **relationship** – Matches, а в **condition** пишем URL нашего сервера с ws.

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/rzgSbgCWurVI4Ej6krBc" alt="" width="375"><figcaption></figcaption></figure></div>

В правом верхнем углу: **троеточие – project setting – save** (тут также надо самому вписать имя файлу и расширение, можно .json)

Сохраняем настройки в файл, чтобы при следующем включении burp выбрать его и не настраивать снова.

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/GqOnzYi8k7KZgkP8HQdm" alt="" width="375"><figcaption></figcaption></figure></div>

### **WebSockets history – просмотр сообщений**

Здесь можно просто смотреть какие сообщения ходят в WebSocket, сортировать по дате, id сокета и т.д.

При нажатии на запрос внизу открывается окно с телом сообщения.

<figure><img src="https://vladislaveremeev.gitbook.io/files/bksKfMmCcYlgT339p348" alt=""><figcaption></figcaption></figure>

### **Intercept – перехват сообщений**

В настройках мы прописали, что надо перехватывать только запросы с адресом вебсокета, поэтому тут теперь просто нажимаем на переключатель: <img src="https://vladislaveremeev.gitbook.io/files/p6YiqngwATNcncv2WgAJ" alt="" data-size="line">

После этого все запросы будут перехватываться и попадать в окно интерсептора, где его можно менять, для отправки нажимаем <img src="https://vladislaveremeev.gitbook.io/files/ilylixfeMXh0L2TsibCH" alt="" data-size="line">

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/OwMUjdxfe8QILshmNnyt" alt="" width="375"><figcaption></figcaption></figure></div>

### **Repeater – отправка сообщений в websocket** <a href="#id-instrumentytestirovaniyawebsocketnaklientakh-repeater-otpravkasoobsheniivwebsocket" id="id-instrumentytestirovaniyawebsocketnaklientakh-repeater-otpravkasoobsheniivwebsocket"></a>

При тестировании вебсокетов нужно кроме перехвата также смотреть кейсы, когда клиенту приходят различные сообщения от вебсокета и как он их обрабатывает. Это удобнее делать напрямую отравляя сообщения в вебсокет клиенту от имени сервера (или наоборот, если понадобиться)

Нажимаем в истории вебсокета правую кнопки мыши на любом запросе в активный вебсокет и выбираем **send to repeater.** Дальше переключаемся на это вкладку (на том же уровне, где и Proxy).

<figure><img src="https://vladislaveremeev.gitbook.io/files/FpcKdVEj3kVQ01Q62tja" alt=""><figcaption></figcaption></figure>

Слева будет окно, куда можно написать своё сообщение, а справа история запросов в websocket.

Здесь также можно оборвать соединение нажав на тумблер.

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/Fn3kjpnBDkYS15LWGAPx" alt="" width="141"><figcaption></figcaption></figure></div>

Можно отправить и редактировать при необходимости в виде Hex. Это полезно если в контракте есть необходимость отправлять конкретные байты вместо текста.

## **ZAP Proxy** <a href="#id-instrumentytestirovaniyawebsocketnaklientakh-zapproxy.1" id="id-instrumentytestirovaniyawebsocketnaklientakh-zapproxy.1"></a>

***

Основные преимущества ZAP перед Burp при работе с websockets:

* показывает PING/PONG сообщения
* при отправке сообщения в websocket можно самостоятельно выбрать тип сообщения (text, binary, ping, pong, close)

Из минусов брейкпоинты обрабатываются последовательно, нельзя увидеть следующий пока не отправишь текущий (ну или я и тут не нашёл где посмотреть). Ну и интерфейс немного старомодный, но по удобности также плох как Burp.

### **Настройки**

Чтобы открыть настройки переходим **ZAP > Settings** или **Tools > Options**

При необходимости язык можно поменять на русский в разделе **Languages.** Применится после перезагрузки.

Переходим в **Network**

#### Local Servers/Proxies <a href="#id-instrumentytestirovaniyawebsocketnaklientakh-localservers-proxies" id="id-instrumentytestirovaniyawebsocketnaklientakh-localservers-proxies"></a>

Адрес оставляем 0.0.0.0 если надо проксировать все входящие соединения.

Порт пишем тот, который используем.

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/lMveWhg7nXIU326a7faN" alt="" width="563"><figcaption></figcaption></figure></div>

#### Server Certificates

Генерируем сертификат (Generate), а потом сохраняем его (Save). Устанавливаем также как и для любых других снифферов.

<div align="left"><figure><img src="https://vladislaveremeev.gitbook.io/files/uxYNTNIsL7SpGQuz7wbI" alt="" width="563"><figcaption></figcaption></figure></div>

### **Просмотр сообщений** <a href="#id-instrumentytestirovaniyawebsocketnaklientakh-prosmotrsoobshenii" id="id-instrumentytestirovaniyawebsocketnaklientakh-prosmotrsoobshenii"></a>

При появлении websocket, вкладка автоматически появляется в нижнем окне. Её можно закрепить нажав на скрепку.

Здесь аналогично burp отображается все запросы во все сокеты, сокетам также присваивается свой id (тут называется **Channel**). Отличие от burp – показываются типы сообщений, а также PING и PONG сообщения.

При нажатии на сообщение тело откроется в окне сверху, можно также посмотреть в виде hex.

<figure><img src="https://vladislaveremeev.gitbook.io/files/IzPXXYdo0cA5UQBQIivx" alt=""><figcaption></figcaption></figure>

### **Перехват запросов**

Для перехвата нажимаем **пкм** на запросе и выбираем **break...**

Перед сохранением можно задать правила перехвата. Например, убрать конкретный канал, указать паттерн пайлоуда и выбрать какие входящие или исходящие сообщения перехватывать.

Поле **Payload Pattern** поддерживает регулярные выражения.

<div align="center"><figure><img src="https://vladislaveremeev.gitbook.io/files/JYNKUGrygLP7QSGBkvch" alt="" width="375"><figcaption></figcaption></figure></div>

При перехвате, запрос появится в верхнем окне, здесь вы его можете модифицировать и отправить. Для **отправки** нажимаем любую стрелку <img src="https://vladislaveremeev.gitbook.io/files/b6rAS7gMxGZJkw97l3bL" alt="" data-size="line">(они хоть и подписаны по разному, но делают тоже самое, отличие только, если вы включили перехват всех запросов (<img src="https://vladislaveremeev.gitbook.io/files/AddATSYNtPrDpylhuhYI" alt="" data-size="line">), тогда при нажатии первой каждый следующий запрос перехватывается, при нажатии второй перехват всех запросов выключается.)

Чтобы удалить сообщение никуда не отправляя нажимаем перечёркнутый круг: <img src="https://vladislaveremeev.gitbook.io/files/gJB859YE0gcjNbwJOb5f" alt="" data-size="line">

<img src="https://vladislaveremeev.gitbook.io/files/5gg2ZV6CickJ84GdvbDW" alt="" data-size="line">– добавить новый брейкпоинт.

<div align="center"><figure><img src="https://vladislaveremeev.gitbook.io/files/Gl9L0n1vYYEwox8ajdkT" alt="" width="563"><figcaption></figcaption></figure></div>

В нижней части экрана, во вкладке **Breakpoints**, можно управлять активными брейкпоинтами.

### **Отправка сообщений в WebSocket** <a href="#id-instrumentytestirovaniyawebsocketnaklientakh-otpravkasoobsheniivwebsocket" id="id-instrumentytestirovaniyawebsocketnaklientakh-otpravkasoobsheniivwebsocket"></a>

Для открытия редактора сообщений нажимаем **пкм** на запросе и выбираем **Open/Resend with Message Editor** или из меню **Tools** > **WebSocket Message Editor.**

Здесь можно выбрать websocket в который отправлять сообщение и направление на клиент – **incoming**, на сервер – **outgoing**.

<figure><img src="https://vladislaveremeev.gitbook.io/files/wfvgYv2wFTtBIgrcpbuA" alt=""><figcaption></figcaption></figure>

Отличие от Burp можно выбрать тип сообщения:

<figure><img src="https://vladislaveremeev.gitbook.io/files/KqgR08VeRgJfZPswAtzl" alt="" width="229"><figcaption></figcaption></figure>
