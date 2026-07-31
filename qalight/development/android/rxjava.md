# RxJava
**Translated Slug:** rxjava
**Source:** [https://qalight.ua/baza-znaniy/rxjava/](https://qalight.ua/baza-znaniy/rxjava/)

---

RxJava

Останнім часом дуже багато захоплюються новим способом створення програмного забезпечення, яке називають реактивним програмуванням. Докотилося воно і до Android. Спробуємо розібратися в цій темі.

Загальна сторінка про реактивне програмування — <http://reactivex.io/>. Документація за класами [тут](http://reactivex.io/RxJava/javadoc/index.html).

Домашня сторінка на GitHub для RxJava — <https://github.com/ReactiveX/RxJava>.

Слід пам’ятати, що компанія Google офіційно не підтримує цей напрямок. Проте деякі програмісти з компанії використовують реактивне програмування у своїх проєктах. Один з них навіть написав свій варіант бібліотеки, схожий з RxJava, який використовувався у одному з додатків Google.

## Перехід на RxJava 2

З деяких пір відбувся поділ версії на дві гілки: 1.x та 2.x.

Гілка 1.x була заморожена 1 червня 2017 року (тільки виправлення багів). 31 березня 2018 року гілку закриють. Я починав вивчати тему на основі 1.x-гілки, тому не дивуйтеся, якщо траплятимуться старі приклади для першої версії. Постараюся явно попереджати про подібні випадки, оскільки відмінності доволі значні.

Різниця між двома гілками описана [на сайті документації](https://github.com/ReactiveX/RxJava/wiki/What's-different-in-2.0). Загальні фундаментальні поняття залишилися тими ж.

Були перейменовані або видалені деякі види класів **Action** та **Function**.

**Subscriber** перейменований у **Disposable**. А також **CompositeSubscription** у **CompositeDisposable**.

## Класи

У RxJava величезна кількість страшних слів, які слід вивчити.

* **Observable**
* **Observer**
* **Subject**, а також **PublishSubject**, AsyncSubject, **BehaviorSubject**, **ReplaySubject**
* **Processor** – підвид **Subject** з підтримкою BackPressure. **AsyncProcessor, BehaviorProcessor, PublishProcessor, ReplayProcessor, UnicastProcessor**.
* **Future**
* **Single** – лінивий еквівалент **Future**.
* **Maybe**
* **Completable**
* **Consumer**
* **Disposable** – минулий **Subscription** з RxJava 1.x
* **Scheduler**
* **Flowable**
