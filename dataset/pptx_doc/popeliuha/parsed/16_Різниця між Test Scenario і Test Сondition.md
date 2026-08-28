# 16_Різниця між Test Scenario і Test Сondition

# Test scenario vs Test condition

## Test Scenario та Test Condition - що спільного?

* One-liners - написані одним реченням і вміщаються в один рядок :)
* Різні форми чек-ліста

![Порівняння Test Condition та Test Scenario](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_2_img_1.jpeg)

![Приклад тест-кейс звіту / чек-листа](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_3_img_1.jpeg)

# Що таке Test Scenario?

* Test scenario — це ймовірний спосіб або метод тестування програми. Тестовий сценарій ставить тестувальника в позицію кінцевого користувача, щоб з'ясувати реальні сценарії та випадки використання програми, що тестується. Його ще називають Test Possibility.
* З Test scenario можна створити Test Conditions, а з них зазвичай створюють Тест Кейси.

![Ієрархія Test Scenario, Test Condition та Test Case](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_6_img_1.jpeg)

## Приклади Test Scenario

**Test Scenario 1:** Check the Login Functionality

Щоб зрозуміти різницю між Test Scenario та Test Cases, нижче наведено приклади Тест кейсів, що можна утворити з цього Test Scenario:

1. Check system behavior when *valid* email id and *password* is entered.
2. Check system behavior when *invalid* email id and *valid* password is entered.
3. Check system behavior when *valid* email id and *invalid* password is entered.
4. Check system behavior when *invalid* email id and *invalid* password is entered.
5. Check system behavior when email id and password are left blank and Sign in entered.
6. Check Forgot your password is working as expected
7. Check system behavior when valid/invalid phone number and password is entered.
8. Check system behavior when “Keep me signed” is checked

![Приклад форми авторизації Amazon](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_8_img_1.jpeg)

- **Test Scenario 2:** Check the Search Functionality
- **Test Scenario 3:** Check the Product Description Page
- **Test Scenario 4:** Check the Payments Functionality
- **Test Scenario 5:** Check the Order History

![Search bar interface](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/image_0.png)

![Приклад інтерфейсу з елементами пошуку та оплати](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_10_img_1.jpeg)

![Orders and Payments Functionality](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_11_img_2.jpeg)

# Що таке Test Condition?

* Елемент або подія компонента або системи, які можуть бути перевірені одним або декількома тестами, наприклад, функція, транзакція, властивість, атрибут якості або структурний елемент.
* Synonyms: test requirement, test situation
* Test condition — це специфікація, якої повинен дотримуватися тестувальник під час тестування програмного забезпечення. Test conditions розроблено на основі реальних тестових ситуацій, а також тестових баз і use case'ів.
* Test condition допомагають переконатися, що програма не містить помилок.

# Приклади Test Condition

* **Test Condition 1:** Leave all fields empty and check registration error messages
* **Test Condition 2:** Put space in the middle of email (`popeliuha @gmail.com`) and check error message
* **Test Condition 3:** Login with valid email and password
* **Test Condition 4:** Verify maximum cart amount by adding 99, 100, 1000, 10000 products
* **Test Condition 5:** Verify that seller is able to add product (mobile device) to catalog

![Форма реєстрації з помилками валідації полів](images/16_Різниця%20між%20Test%20Scenario%20і%20Test%20Сondition/page_15_img_1.jpeg)

## Відмінності між Test Scenario і Test Condition

### Test Scenario

1. Один Scenario може містити кілька Conditions.
2. Тестовий сценарій охоплює широкий спектр можливостей.
3. Хороший тестовий сценарій допомагає зменшити складність.
4. Визначивши тестові сценарії, можна легко зрозуміти функціональність продукту.
5. Зазвичай тестовий сценарій охоплює функціональність, атрибути, інші функції та аспекти програмного продукту.
6. Для визначення тестового сценарію потрібно порівняно менше часу.
7. Тестовий сценарій може складатися з одного рядка, щоб пояснити, що ми збираємося тестувати.
8. Наприклад, тестовим сценарієм може бути вхід на домашню сторінку будь-якого сайту.

### Test Condition

1. Один Condition можна виконати одним або декількома Test Case'ами.
2. Test Conditions - це дуже детальне тестування будь-якого тестового сценарію.
3. Хороші Test Conditions допомагають уникнути помилок програми.
4. Виконуючи різні Test Conditions, можна дізнатися, чи добре працює програма.
5. Зазвичай Test Condition охоплює набір вхідних даних, очікуваних результатів, точних виходів тощо для перевірки певної функції.
6. Для тестування будь-якого Test Condition потрібно порівняно більше часу.
7. Test Condition зазвичай теж one-liner'и, але з них можна створити один або кілька Test Case'ів, щоб перевірити, як ми збираємося тестувати.
8. Наприклад, для перевірки Test Condition входу умовами тестування можуть бути дійсний ідентифікатор користувача та дійсний пароль, дійсний ідентифікатор користувача та недійсний пароль, недійсні ідентифікатор користувача та пароль тощо.

