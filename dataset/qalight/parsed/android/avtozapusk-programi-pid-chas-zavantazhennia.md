# Автозапуск програми під час завантаження

**Source:** https://qalight.ua/baza-znaniy/avtozapusk-programi-pid-chas-zavantazhennya/

---

Автозапуск програми під час завантаження

Тема отримання повідомлення **ACTION\_BOOT\_COMPLETED** залишається актуальною і до цього дня. Багато новачків стикаються з проблемою: вони не отримують у своїх додатках даного повідомлення.

Можна виділити наступні правила:

У маніфесті вказати дозвіл:

`<uses-permission android:name=”android.permission.RECEIVE\_BOOT\_COMPLETED” />`

У маніфесті в блоці **application** зареєструвати приймач на прийом повідомлення **ACTION\_BOOT\_COMPLETED**:

`<receiver android:name=”.MyBroadcastReceiver”>`

`<intent-filter>`

`<action android:name=”android.intent.action.BOOT\_COMPLETED” />`

`</intent-filter>`

`</receiver>`

В описі без необхідності не вказуйте атрибути «enabled», «exported» і т.д. Цілком достатньо налаштувань і атрибутів за замовчуванням.

Код вашого широкомовного приймача:

public class BootCompletedReceiver extends BroadcastReceiver {

public BootCompletedReceiver() {

}

public void onReceive(Context context, Intent intent) {

if (intent.getAction().equals(Intent.ACTION\_BOOT\_COMPLETED)) {

// ваш код тут

}

}

}

Якщо ваш приймач використовується тільки для повідомлення **ACTION\_BOOT\_COMPLETED**, то перевірка «if» не обов’язкова. Однак іноді розробники використовують один і той же ресивер для різних повідомлень. В цьому випадку фільтруйте повідомлення, перевіряючи їх усередині методу **onReceive()**.

Додаток повинен бути встановлений на внутрішню пам’ять. Android влаштовано таким чином, що повідомлення **ACTION\_BOOT\_COMPLETED** відправляється додаткам перед монтуванням зовнішній пам’яті. Тому додатки, встановлені на зовнішній пам’яті, ніколи не отримають це повідомлення. Щоб вказати системі не встановлювати додаток на зовнішню пам’ять, у маніфесті НЕ потрібно прописувати для атрибута «@android: installLocation» значення «auto» або «preferExternal». За замовчуванням, тобто якщо цей атрибут не вказаний, Android встановить вашу програму тільки на внутрішню пам’ять. Однак згідно з офіційною документацією краще явно вказати значення «internalOnly», щоб у вас та інших розробників не виникло спокуси в майбутньому вказати інше значення.

<manifest xmlns:android=”http://schemas.android.com/apk/res/android”

android:installLocation=”internalOnly”

… >

Після встановлення або примусової зупинки (force stop) програма повинна бути запущена хоча б один раз, щоб система «запам’ятала» цей додаток для відправки йому повідомлення **ACTION\_BOOT\_COMPLETED**. Таку поведінку було реалізовано у версії Android 3.1 з міркувань безпеки. В чому суть? Усі нещодавно встановлені програми знаходяться в стані «stopped» (не плутати з активіті, тому що система по-різному керує цим станом у додатках і активностях). У цей же стан додаток «переходить», коли користувач у налаштовуваннях телефону примусово його зупиняє. Поки додаток знаходиться в такому стані, він не буде запускатися системою з жодної причини (наприклад, через **ACTION\_BOOT\_COMPLETED**), виключаючи, звичайно ж, запуск самим користувачем. Завдяки такому нововведенню чимала частина вірусів і троянців» перестала працювати, тому що вже неможливо запуститися автоматично після встановлення.

Виняток становлять системні додатки.

Особливості режиму Fast boot в HTC-пристроях: Відомо, що HTC-пристрої не перезавантажуються у класичному розумінні, а використовують так званий режим Fast boot (це одна з форм глибокого сну), зберігаючи стан ОС на диск. Тому повідомлення **ACTION\_BOOT\_COMPLETED** не надсилається системою, оскільки насправді перезавантаження не відбувається. Замість **ACTION\_BOOT\_COMPLETED** система може відправити наступні повідомлення:

`<action android:name=”android.intent.action.QUICKBOOT\_POWERON” />`

`<action android:name=”com.htc.intent.action.QUICKBOOT\_POWERON” />`

У вашому додатку вкажіть у тезі «receiver» крім **ACTION\_BOOT\_COMPLETED** також вказані вище повідомлення. Крім цього необхідно прописати додатковий дозвіл:

`<uses-permission android:name=”android.permission.QUICKBOOT\_POWERON” />`

## Практика: помилки та особливості експлуатації

Розберемо помилки, які роблять новачки під час налаштування програми й у коді.

* Після встановлення або force stop додаток жодного разу не запускався.
* Додаток встановлено не на внутрішній пам’яті, або користувач вручну переніс його на зовнішню пам’ять.
* В окремих розробників прийом починав працювати, коли вони вказували відносне ім’я класу приймача.
* Також окремі розробники у Logcat не бачили своїх повідомлень з ресивера. Використовуйте Toast для налагодження:

Toast toast = Toast.makeText(context.getApplicationContext(),

context.getResources().getString(R.string.your\_message), Toast.LENGTH\_LONG);

toast.show();

* Помилки або неіснуючі повідомлення всередині тега ресивера:
* Неправильне положення елементів у маніфесті програми:  
  «uses-permission» повинен бути вказаний тільки як прямий нащадок елемента «manifest», не потрібно його вказувати/дублювати у тезі «receiver»;  
  тег «receiver» повинен бути вказаний тільки як прямий нащадок елемента «application».
* Різні диспетчери завдань, оптимізатори, додатки безпеки, Startup-менеджери і т.п. можуть відстежувати реєстрацію програми для прийому **ACTION\_BOOT\_COMPLETED**і забороняти/дозволяти його отримання під час завантаження. Видаліть ці додатки або додайте у виняток вашу програму в її налаштовуваннях.
* Як зазначалося вище, окремі пристрої використовують режим Fast boot. Можна спробувати в налаштовуваннях телефону відключити цей режим.
* У додатку відсутня будь-яка активність, тому після встановлення у користувача немає можливості хоча б один раз запустити вашу програму. Через це повідомлення **ACTION\_BOOT\_COMPLETED**НЕ буде відправлене до вашої програми.
* Помилки немає, але все ж: вказані зайві, необов’язкові атрибути у тезі «receiver», наприклад («uses-permission», «enabled», «exported») (Примітка від мене: сумнівна порада, у мене працювало):

<receiver

android:name=”.BootCompletedReceiver”

android:enabled=”true”

android:exported=”true” >

`<uses-permission android:name=”android.permission.RECEIVE\_BOOT\_COMPLETED” />`

`<intent-filter>`

`<action android:name=”android.intent.action.BOOT\_COMPLETED” />`

`</intent-filter>`

`</receiver>`

## Налагодження ресивера в емуляторі та на реальних пристроях

У терміналі виконайте:

adb shell

Далі, щоб відправити **ACTION\_BOOT\_COMPLETED** всіх програм, наберіть у терміналі:

am broadcast -a android.intent.action.BOOT\_COMPLETED

Або для відправки **ACTION\_BOOT\_COMPLETED** певної програми наберіть у терміналі:

am broadcast -a android.intent.action.BOOT\_COMPLETED your.package.name

В емуляторі: встановіть ваше ПЗ, запустивши його зі студії. При цьому студія збере ваш проєкт, встановить додаток і запустить його. Після цього закрийте емулятор (це аналогічно вимкненню на реальному пристрої). Щоб отримати повідомлення ACTION\_BOOT\_COMPLETED, запустіть емулятор з AVD-менеджера, а не за допомогою кнопки «Run app» у студії.

Після запуску емулятора на вкладці Android Monitor вкажіть запущений емулятор і ваш додаток, щоб переглянути логи logcat.

## Підсумки

Щоб ваш додаток запускався під час завантаження на всіх пристроях, маніфест як мінімум повинен виглядати наступним чином:

`<?xml version=”1.0″ encoding=”utf-8″?>`

<manifest xmlns:android=”http://schemas.android.com/apk/res/android”

android:installLocation=”internalOnly”

package=”com.site.yourapp” >

`<uses-permission android:name=”android.permission.RECEIVE\_BOOT\_COMPLETED” />`

`<uses-permission android:name=”android.permission.QUICKBOOT\_POWERON” />`

`<application>`

<activity

android:name=”.MainActivity”

android:label=”@string/app\_name” >

`<intent-filter>`

`<action android:name=”android.intent.action.MAIN” />`

`<category android:name=”android.intent.category.LAUNCHER” />`

`</intent-filter>`

`</activity>`

<receiver

android:name=”.BootCompletedReceiver” >

`<intent-filter>`

`<action android:name=”android.intent.action.BOOT\_COMPLETED” />`

`<action android:name=”android.intent.action.QUICKBOOT\_POWERON” />`

`<action android:name=”com.htc.intent.action.QUICKBOOT\_POWERON” />`

`</intent-filter>`

`</receiver>`

`</application>`

`</manifest>`

Код ресивера, як правило, буде таким:

public class BootCompletedReceiver extends BroadcastReceiver {

public BootCompletedReceiver() {

}

public void onReceive(Context context, Intent intent) {

if (intent.getAction().equals(Intent.ACTION\_BOOT\_COMPLETED)) {

Toast toast = Toast.makeText(context.getApplicationContext(),

context.getResources().getString(R.string.your\_message), Toast.LENGTH\_LONG);

toast.show();

Log.d(“myapp”, context.getResources().getString(R.string.your\_message);

// ваш код тут

}

}

}