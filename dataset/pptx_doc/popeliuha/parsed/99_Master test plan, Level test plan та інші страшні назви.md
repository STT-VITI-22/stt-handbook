# 99_Master test plan, Level test plan та інші страшні назви

# Master Test Plan

# Level Test Plan

# etc.

# Junior, Junior Pro Level *(a.k.a. Test Manager Advanced)*

* Master Test Plan (MTP) and Level Test Plan (LTP)
* Level Test Design (LTD)
* Master Test Report (MTR) and Level Test Report (LTR)
* Test Summary Report (TSR)
* Level Test Case (LTC)
* Level Procedure (LP)
* Anomaly Report (AR)
* Check List (non-standardized)

# Software test documentation

* **Master Test Plan**: an overall test planning and test management document for multiple levels of test.
* **Level Test Plan**: approach, resources, and schedule of the testing activities for each specified level of testing need to be described.
* **Level Test Design (LTD)**: Detailing test cases and the expected results as well as test pass criteria.
* **Level Test Case (LTC)**: Specifying the test data for use in running the test cases.
* **Level Test Procedure (LTPr)**: Detailing how to run each test, including any set-up preconditions and the steps that need to be followed.
* **Level Test Log (LTL)**: To provide a chronological record of relevant details about the execution of tests, e.g. recording which tests cases were run, who ran them, in what order, and whether each test passed or failed.
* **Anomaly Report (AR)**: Defect, trouble, issue, anomaly, or error report. These include the expected results being wrong, the test being run incorrectly, or inconsistency in the requirements.
* **Level Interim Test Status Report (LITSR)**: To summarize the results of the testing activities and optionally to provide evaluations and recommendations based on the results for the specific test level.
* **Level Test Report (LTR)**: To summarize the results of the designated testing activities and to provide evaluations and recommendations based on the results after test execution has finished for the specific test level.
* **Master Test Report (MTR)**: A management report providing any important information uncovered by the tests accomplished, and including assessments of the quality of the testing effort, the quality of the software system under test, and statistics derived from Anomaly Reports. The report also records what testing was done and how long it took, in order to improve any future test planning. This final document is used to indicate whether the software system under test is fit for purpose according to whether or not it has met acceptance criteria defined by project stakeholders.

# Тестова документація та робочі продукти

Документація часто створюється як частина діяльності з управління тестуванням. Незважаючи на те, що конкретні назви документів керування тестуванням і обсяг кожного документа, як правило, відрізняються, нижче наведено типові типи документів керування тестуванням, які зустрічаються в організаціях і проектах:

* **Test policy** - описує цілі організації та цілі тестування
* **Test strategy** - описує загальні, незалежні від проекту методи тестування організації
* **Master test plan (or project test plan)** - описує реалізацію стратегії тестування для конкретного проекту
* **Level test plan (or phase test plan)** - описує конкретні дії, які необхідно виконати на кожному рівні тесту

Фізичне розміщення цих типів документів може відрізнятися залежно від контексту. У деяких організаціях і на деяких проектах вони можуть бути об'єднані в один документ; в інших вони можуть бути знайдені в окремих документах; а в деяких їх зміст може проявлятися як інтуїтивні, неписані або традиційні методології тестування.

Більші та більш офіційні організації та проекти, як правило, мають усі ці типи документів як письмові робочі продукти, тоді як менші та менш формальні організації та проекти, як правило, мають менше таких письмових робочих продуктів.

# Master Test Plan

Master test plan охоплює всю роботу з тестування, яка має бути виконана в конкретному проекті, включно з конкретними рівнями, які необхідно виконати, і зв'язками між цими рівнями, а також між рівнями тестування та відповідними заходами розробки.

У master test plan має бути обговорено, як тестувальники реалізовуватимуть стратегію тестування для цього проекту (тобто тестовий підхід). Master test plan має відповідати test policy та strategy, а в окремих областях, де це не так, має пояснювати ці відхилення та винятки, включаючи будь-який потенційний вплив, спричинений відхиленнями.

Наприклад, якщо стратегією тестування організації є проведення одного повного регресійного тестування на незмінній системі безпосередньо перед випуском, але поточний проект не матиме регресійного тестування, у плані тестування має бути пояснено, чому це планується та що буде зроблено для пом'якшення будь-якого ризику через це відхилення від звичайної стратегії.

У невеликих проектах, де формалізовано лише один рівень тестування, master test plan та test plan для цього формалізованого рівня часто об'єднуються в один документ.

Крім того, тестування зазвичай залежить від інших дій у проекті. Якщо ця діяльність недостатньо задокументована, особливо з точки зору її впливу та зв'язку з тестуванням, теми, пов'язані з цією діяльністю, можуть бути охоплені в master test plan (або в плані тестування відповідного рівня). Наприклад, якщо процес керування конфігурацією не задокументовано, у плані тестування має бути вказано, як тестові об'єкти мають бути доставлені команді тестування.

# Master Test Plan

Хоча конкретний зміст і структура генерального плану тестування змінюється залежно від організації, її стандартів документації та формальності проекту, типові теми для генерального плану тестування включають:

* Елементи, які підлягають і не підлягають тестуванню
* Характеристики якості, які підлягають і не підлягають тестуванню
* Графік і бюджет тестування (який повинен бути узгоджений з проектом або операційним бюджетом)
* Цикли виконання тестів та їх зв'язок із планом релізу програмного забезпечення
* Відносини та результати між тестуванням та іншими людьми чи відділами
* Визначення того, які елементи тесту знаходяться в межах і поза межами для кожного описаного рівня
* Конкретні критерії входу, критерії продовження (призупинення/відновлення) і критерії виходу для кожного рівня та зв'язки між рівнями
* Ризики тестового проекту
* Загальне управління тестуванням
* Відповідальність за виконання кожного рівня тесту
* Входи та виходи з кожного рівня тесту

# Level Test Plan

Level test plans описують конкретні дії, які необхідно виконати в межах кожного рівня тесту або, в деяких випадках, типу тесту. 

Level test plans доповнюються, якщо це необхідно, до master test plan для конкретного рівня або типу тесту, який документується. Вони містять деталі розкладу, завдань і етапів, які не обов'язково охоплюються master test plan. Крім того, оскільки різні стандарти та шаблони застосовуються до специфікації тестів на різних рівнях, ці деталі будуть охоплені планами тестування рівня.

У менш формальних проектах або операціях план тестування часто є єдиним документом для керування тестуванням. У таких ситуаціях деякі з інформаційних елементів, згаданих раніше в цьому розділі, можна охопити в цьому документі плану тестування.

Для гнучких проектів плани тестування рівня можуть замінити плани спринту або ітераційного тестування.

