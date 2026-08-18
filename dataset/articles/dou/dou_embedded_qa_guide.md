# dou_embedded_qa_guide

<p>Вітаю, спільното! Я Влад Величко, зі своїх 13 років у QA останні три працюю з Embedded-напрямом у SQUAD. Маю сертифікації ISTQB (Foundation Level, Advanced Test Analyst, Advanced Test Manager), а ще — досвід роботи на позиціях Support Lead та Project Manager.</p>

<p>Ділюся з вами дослідженням про найпопулярніші скіли Embedded QA, яке ми робили в SQUAD. У жовтні ми презентували результати на офлайн-події єТЕМА (<a href="https://www.youtube.com/live/EgIw_CAnFhA?si=4RevEuMEqM6N9iio" target="_blank">запис</a> можна переглянути на нашому YouTube-каналі), а в цьому матеріалі я наведу свіжі дані за третій квартал 2024 року.</p>

<h2>Методологія дослідження та збір даних</h2>

<p>Перед нами постали запитання: як залишатися в топі професійних профільних знань, які навички зараз мають найбільший попит та як зрозуміти, що потрібно розвивати? Отож ми взялися це дослідити.</p>

<p>Передусім потрібно було вирішити, де і що ми шукаємо, адже платформи IT-вакансій в Україні та США — різні. Наші локальні всім відомі: Djinni, DOU, LinkedIn. Серед топових американських платформ — той самий LinkedIn, Dice, Indeed, StackOverflow. </p>

<p>Оскільки нам необхідно було відокремити вакансії розробників від вакансій тестувальників, ми розглянули пошукові запити. Спочатку спробували «Embedded QA», але знайшли дуже маленьку кількість вакансій. Тож вирішили себе перевірити: ввели в пошук лише слово «Embedded» — й отримали вакансії Embedded QA, Embedded Tester, Test Engineer, QA/Quality Assurance Engineer. </p>

<p>Правильні запити допомагають нічого не пропустити, звузити результати пошуку та зменшити кількість нерелевантних вакансій. І ще один очевидний момент: деякі вакансії на платформах повторюються, тому потрібно пильнувати й відсіювати дублікати.</p>

<p>Сумарно вийшло близько 200+ вакансій. QA-позицій виявилося значно менше, ніж здавалось на перший погляд. Вакансій розробників було в рази більше. Проте, на мою думку, цього вистачило, щоб побачити загальну тенденцію на ринку.</p>

<p><img src="https://s.dou.ua/storage-files/image_4055938861735054454452.png"></p>

<p>Наступний етап — найвеселіший: переглядати те, що нафільтрували. Ви навіть не уявляєте, чого я там начитався. <strong>Знайшов, зокрема, й омріяну мною з дитинства позицію QA-космонавта.</strong></p>

<p>Отже, діяв я таким чином: перечитував вакансії та їхні вимоги, а потім робив собі короткий конспект, записуючи посилання, компанію, позицію і необхідні навички. Тут хочу ще раз звернути увагу, що вакансії на різних платформах дублюються. Оскільки робота тривала не один день, а пам’ять у мене — як у браузера Google Chrome (має властивість закінчуватись), я проводив пошук за назвою компанії задля уникнення повторів. Якщо ж такі траплялися, то порівнював вакансії. Деякі компанії дійсно мали кілька різних пропозицій. </p>

<p><img src="https://s.dou.ua/storage-files/image_51371716251735054454450.png"></p>

<p>Після опрацювання всіх вакансій ідемо за конспектом і робимо табличку: скіл vs посилання. Рахуємо повтори кожної навички за посиланнями та сортуємо за їхньою кількістю. </p>

<h2>Загальні результати дослідження та потреби ринку</h2>

<p>Коли ми аналізували статистичні дані з обох ринків, найперше стала очевидною гостра потреба не просто в мануальних QA-інженерах, а в спеціалістах General QA. </p>

<p>Якщо коротко, General QA — це універсальний фахівець, який має ширшу експертизу. Можна сказати, QA 2.0. Він здатен виконувати не тільки мануальне, а й автоматизоване тестування: запускати готові скоупи, робити мінорні фікси й додавати автотести. </p>

<p><img src="https://s.dou.ua/storage-files/image_12486262171735054454454.png"></p>

<p>Перші три позиції переліку топових навичок підтверджують наше спостереження: мова програмування Python, розуміння CI/CD-процесів та досвід автоматизованого тестування. </p>

<p>Усі ми знаємо, що автоматизація на проєкті суттєво заощаджує час на регресійне тестування, дозволяє уникнути повторних ручних прогонів, які зазвичай затяжні. Завдяки автоматизації тести можна виконувати швидше і частіше, що забезпечує ефективніший контроль якості та прискорює процес розробки й виходу продуктів на ринок.</p>

<p>Далі за списком у нас класичні навички Embedded-тестувальника: розуміння роботи RTOS (операційних систем реального часу), включно з управлінням завданнями, таймінгами та синхронізацією. Знання Linux-дистрибутивів (наприклад, Yocto або Buildroot) дозволяє налаштовувати середовище, аналізувати логи та виконувати діагностику. Bash-скриптинг необхідний для автоматизації рутинних процесів, як-от запуск тестів чи збір даних. А володіння мовами C і C++ дає змогу глибше аналізувати код, писати низькорівневі тести та знаходити приховані проблеми.</p>

<p>До топу також потрапили навички, пов’язані з апаратним забезпеченням: взаємодія між залізом і софтом, знання мікропроцесорів та їхньої архітектури, вміння використовувати різні апаратні інструменти для тестування і читати електронні схеми.</p>

<p><img src="https://s.dou.ua/storage-files/image_27688161441735054454448.png"></p>

<p>Крім основних технічних знань, увагу приділяють і менш поширеним, але не менш важливим навичкам на кшталт обробки відео й зображень, RESTful API тощо. Це говорить про те, що спеціалісти в Embedded QA часто мають працювати на стику різних дисциплін і володіти широким спектром технічних знань.</p>

<p>Розглянемо глибше ці навички на ринках України та США.</p>

<h2>Порівняння ринків України та США</h2>

<p>Якщо коротко, все дуже схоже: ми відповідаємо світовим тенденціям і майже не відрізняємося від країн, які задають тренд. Навички, які мають попит у США, популярні й у нас. І це стосується не тільки QA-домену, а й IT загалом. Але є і певні відмінності.</p>

<p><img src="https://s.dou.ua/storage-files/image_19237647421735054454408.png"></p>

<p>Вакансії в США здебільшого орієнтовані на внутрішній ринок, тоді як українські, як правило, спрямовані на міжнародні ринки та аутсорс. Працюючи на зовнішні ринки, українські спеціалісти набувають досвіду в різноманітних проєктах, що може підвищити їхню цінність на ринку праці. Адаптивність і здатність до комунікації з командами з різних країн дає українським тестувальникам додаткову перевагу в міжнародній площині. Водночас у США кар’єрний шлях може бути чіткіше окресленим, але з меншими можливостями розвитку.</p>

<p>На відмінності у сфері Embedded QA впливає війна: стрімкого розвитку набуває miltech і все, що він передбачає, а саме — підвищені вимоги до знання апаратної частини, забезпечення надійності та безпеки комунікацій. Стають необхідними навіть такі навички, як пайка. Потреба в ремонті та підтримці апаратних компонентів у польових умовах вимагає від фахівців вміння швидко й ефективно виконувати такі завдання.</p>

<p>З цікавого у вакансіях, що не відобразиш на графіку:</p>

<ul><li>США. Часто серед вимог до кандидата ледь не на першому місці — вища освіта в галузі комп’ютерних наук або інженерії.</li><li>Україна. У сфері QA формальна освіта не є визначальним фактором. Перевагу мають практичні навички, реальний досвід і безперервне навчання, особливо через тренінги та онлайн-курси.</li></ul>

<p><strong>Це показує, що для українських QA-фахівців важливіше бути в курсі актуальних технологій і методологій, ніж мати академічний ступінь.</strong> Таким чином акцент на практичному досвіді дає тестувальникам змогу швидше адаптуватися до змінних вимог ринку і залишатися затребуваними.</p>

<p>Підіб’ємо підсумки. Обидва ринки мають схожі тенденції та вимагають подібних навичок, але наші спеціалісти володіють, крім високого рівня професіоналізму, здатністю швидко адаптуватися. Та використовують нестандартні підходи попри нестабільність в умовах війни.</p>

<h2>Актуальні ключові напрями Embedded QA</h2>

<p>Для зручності ми обʼєднали та класифікували навички з основного списку за напрямами:</p>

<ul><li>Automation skills</li><li>Networking / Connectivity skills</li><li>Hardware-related skills</li><li>QA domain &amp; General skills</li></ul>

<p><img src="https://s.dou.ua/storage-files/image_87338659681735054454456.png"></p>

<p>Розглянемо їх докладніше.</p>

<h3>Automation skills</h3>

<p>До них належать:</p>

<ul><li>Уміння проєктувати та впроваджувати фреймворки автоматизації в тестування.</li></ul>

<p>У деяких вакансіях йдеться про побудову процесу автоматизації з нуля або інтеграцію певного інструменту в проєкт, що вже існує.</p>

<ul><li>Знання мов програмування, таких як Python, C/C++ або Java, які використовують для розробки автоматизованих тестових скриптів.</li></ul>

<p><strong>Як ми побачили зі статистики, вимога знати Python та С/C++ трапляється дуже часто.</strong> Але першість за Python. Java і С# — менш популярні. До речі, ще до дослідження ми у SQUAD взялися вивчати Python для власних внутрішніх потреб. Тоді це рішення було більш інтуїтивним. Зараз, коли є результати дослідження, маємо обґрунтування.</p>

<ul><li>Розуміння, що таке Continuous Integration і Continuous Delivery та які їхні інструменти: Git, Jenkins, Make, CMake тощо.</li></ul>

<h3>Networking / Connectivity skills</h3>

<p>Базові знання мереж:</p>

<ul><li>Концепції багаторівневих моделей OSI та TCP/IP: що описують, які дані на різних рівнях.</li></ul>

<ul><li>Основні протоколи, такі як TCP (Transmission Control Protocol), UDP (User Datagram Protocol), HTTP/HTTPS, DNS, DHCP, FTP та інші.</li></ul>

<ul><li>Відмінності між дротовими (Ethernet) і бездротовими (Wi-Fi) мережами, їхня конфігурація та стандарти (наприклад, 802.11 для Wi-Fi). Вміння побудувати та налаштувати мережу.</li></ul>

<ul><li>Основи маршрутизації. Куди і як іде трафік. Як працюють мережеві пристрої. Тегований трафік і таке інше.</li></ul>

<ul><li>Безпека: використання VPN та firewall. Правила фільтрування та блокування трафіку, відкриті й закриті порти.</li></ul>

<ul><li>Інструменти: використання мережевих сніферів та аналайзерів. TCPdump/Wireshark тощо.</li></ul>

<p>Connectivity:</p>

<ul><li>Тестування окремих протоколів підключення та знання їхніх стандартів. Наприклад: Wi-Fi базується на стандарті IEEE 802.11. Потрібно знати основні версії, частоти, специфіку роботи (фізика), плюси й мінуси, де який краще використовувати.</li></ul>

<ul><li>Тестування пристроїв з паралельним/одночасним підключенням через декілька протоколів. Це процес перевірки й оцінки роботи пристроїв, які можуть підключатися та взаємодіяти з іншими пристроями або мережами через різні комунікаційні протоколи одночасно.</li></ul>

<ul><li>Connectivity-тести з використанням багатьох виробників і моделей роутерів. Interoperability. Наприклад: під час тестування Wi-Fі-підключення потрібно переконатися, що тестовий пристрій може під’єднатися до роутерів усіх виробників (адже в їхніх прошивках і протоколах підключення є певні особливості та нюанси).</li></ul>

<h3>Hardware-related skills</h3>

<p>Тепер розглянемо апаратну частину. Щоб задовольняти запити ринку, фахівцям Embedded QA необхідні:</p>

<ul><li>Базове розуміння електроніки й схемотехніки, принципів роботи радіочастотних (RF) схем, а також уявлення про поширення сигналів та модуляцію.</li></ul>

<ul><li>Розуміння роботи системи на чипі: від апаратної архітектури до операційної системи.</li></ul>

<ul><li>Глибоке знання мікроконтролерів, таких як STM32, Realtek, та досвід роботи з архітектурою Cortex.</li></ul>

<ul><li>Розуміння периферійних пристроїв (UART, SPI, I2C тощо) та їхньої інтеграції в системи.</li></ul>

<ul><li>Досвід роботи із SDK: Nordic nRF5/nRF Connect.</li></ul>

<ul><li>Вміння використовувати осцилографи, logic analyzers, мультиметри та лабораторні блоки живлення.</li></ul>

<ul><li>Базові навички пайки.</li></ul>

<h2>QA domain &amp; General skills</h2>

<p>Ну і, нарешті, останнє, але не менш важливе — «домен тестування». Бо хай які панують світові тренди, без бази нічого не вийде.</p>

<p>Сюди належать знання основ тестування (теорія та основні процеси), різні типи тестування (функціональне, регресійне тощо), методології розробки (Agile, Waterfall) і стандарти. А ще — процеси управління тестуванням, аналіз вимог, техніки тест-дизайну, написання тест-кейсів та знання життєвого циклу розробки (SDLC). Не менш важлива тестова документація: тест-плани, звіти й баг-репорти.</p>

<p>До базових вимог ми зарахували й знання з RTOS та Embedded Linux-дистрибутивів та RESTful API тестування (Postman, GET, POST, PUT, DELETE тощо).</p>

<p>Отож ми маємо список навичок — ідемо далі.</p>

<h2>Пріоритезація навичок для компанії</h2>

<p>Сформований список ми адаптували у SQUAD згідно з нашими потребами і пропустили через призму власних проєктів. Це дозволило точніше підлаштувати навички під наявні завдання та почати використовувати здобуті знання на практиці. Відповідно, для іншої компанії список може відрізнятися.</p>

<p>Результати дослідження ми розділили на два списки навичок. Деякі з них ми вже маємо, деякі потребують розвитку та покращення, а опанування інших — у процесі або заплановано. Менш важливі, на нашу думку, або дуже специфічні скіли відклали на потім, у другий список, як можливість для майбутнього розвитку. </p>

<p><strong>Наведу приклад.</strong> Незважаючи на те, що в загальному топі лідирують С/C++, а Java — трохи нижче в списку, ми їх депріоритезували й підняли Java. Вона нам потрібна для проєктів, які вже в роботі. Важливо не тільки здобути нові знання, а й утримати їх. Якщо їх не використовувати, то вони просто забудуться.</p>

<p>Відтак ми провели голосування серед лідів нашого департаменту, щоб відсортувати скіли за важливістю. Нижче на зображенні — найзначущіші для нас навички. Чому всього 15? Бо треба з чогось починати. Навичок багато, але хапатися за все й одразу — значить не зробити нічого.</p>

<p><strong></strong></p>

<p><img src="https://s.dou.ua/storage-files/image_13939233531735054454429.png"></p>



<h2>Побудова skill set матриці команди</h2>

<p>Отож дослідження проведено, список навичок є. Наступний крок — оцінити, де ми знаходимось на шкалі сучасного Embedded QA. Для цього ми використали не новий, але перевірений часом інструмент — skill set матрицю. </p>

<p>Але чому саме її? Як ми будували skill set матрицю команди та оцінювали наших інженерів і інженерок? Та як, зрештою, ефективно використовувати здобуті знання в майбутньому?</p>

<p>Відповіді на ці питання можна знайти вже у <a href="https://www.youtube.com/live/EgIw_CAnFhA?si=0ZatoWmaJBZUUBwY&amp;t=3438" target="_blank">виступі</a> моєї колеги Каті Подлеснюк, QA Manager. Вона детально аналізує і демонструє, як це виглядає на практиці та скільки всього корисного можна взяти з цих знань.</p>



			<p style="background: #ffd;outline: 1px solid #dd3;padding: 10px 20px;margin-bottom: 17px;">
Сподобалась стаття?				<a rel="nofollow" href="https://dou.ua/users/vladislav-velichko-3/subscribe-author/follow/" style="border-bottom:1px solid;">Підписуйтесь на автора</a>, щоб отримувати сповіщення про нові публікації на пошту.</p>


			<div class="b-post-tags">
				<span class="title">Теми:</span> <a href="https://dou.ua/forums/tags/automation%20QA/">automation QA</a>, <a href="https://dou.ua/forums/tags/C++/">C++</a>, <a href="https://dou.ua/forums/tags/embedded/">embedded</a>, <a href="https://dou.ua/forums/tags/hardware/">hardware</a>, <a href="https://dou.ua/forums/tags/QA/">QA</a>, <a href="https://dou.ua/forums/tags/%D0%B4%D0%BE%D1%81%D0%BB%D1%96%D0%B4%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F/">дослідження</a>
			</div>
	</article>


		
	<div class="likely" data-url="https://dou.ua/forums/topic/51761/" data-title="Від Python до пайки: аналізуємо топскіли для Embedded QA">


			<div id="btnLike" class="likely__widget likely__widget_likes "><span class="likely__icon likely__icon_likes" style="opacity: .6;filter: grayscale(0.6);position: relative; left:2.5px;">👍</span><span class="likely__button likely__button_likes"><span class="unchecked_text">Подобається</span><span class="checked_text">Сподобалось</span></span><span class="likely__counter">13</span></div>

			<div id="btnStar" class="likely__widget likely__widget_stars "><span class="likely__icon likely__icon_stars"><svg class="likely__star_empty" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path id="Shape" d="m15.965661,6.219396l-5.74046,-0.49252l-2.24237,-5.290234l-2.24237,5.290234l-5.740461,0.49252l4.354623,3.7735l-1.305176,5.611125l4.933383,-2.975997l4.933383,2.975997l-1.305177,-5.611125l4.354624,-3.7735l0,0zm-7.982831,4.911043l-3.00394,1.812119l0.795092,-3.417455l-2.652693,-2.297475l3.496484,-0.300136l1.365057,-3.22188l1.365057,3.22188l3.496484,0.300136l-2.651889,2.297475l0.795092,3.417455l-3.004743,-1.812119l0,0z"/></svg><svg class="likely__star_full" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path id="Shape" d="m7.994121,12.627484l4.927092,2.959405l-1.303512,-5.581348l4.349073,-3.753476l-5.733144,-0.489906l-2.23951,-5.262159l-2.239511,5.262159l-5.733142,0.489906l4.349071,3.753476l-1.303512,5.581348l4.927094,-2.959405z"/></svg></span><span class="likely__button likely__button_stars"><span class="unchecked_text">До обраного</span><span class="checked_text">В обраному</span></span><span class="likely__counter">6</span></div>

			<div class="facebook" title="Поділитись посиланням на Фейсбуці">Facebook</div>
			<div class="twitter" title="Поділитись посиланням в Твіттері" data-via="dou_forum">Twitter</div>
			<div class="linkedin" title="Поділитись посиланням в LinkedIn">LinkedIn</div>
	</div>


		<script>
			impressions.push({'pageviews-content': 123585});
		</script>



				<div class="b-similar-topics">
					<h4>Схожі статті</h4>
					<ul>
							<li><a href="https://dou.ua/lenta/articles/language-rating-2026/?from=similar_posts_blogs">Рейтинг мов програмування 2026. TypeScript зростає, Python — лідер серед новачків</a></li>
							<li><a href="https://dou.ua/lenta/articles/analytics-youtube-23/?from=similar_posts_blogs">Рекордні ЗП у QA | Бум в DefTech | Шанси джунів у 2026 📈</a></li>
							<li><a href="https://dou.ua/lenta/articles/deftech-jobs-analitycs-q1-2026/?from=similar_posts_blogs">Оборонні компанії почали активніше наймати — аналітика вакансій</a></li>
							<li><a href="https://dou.ua/lenta/articles/how-ai-changes-qa-junior-work/?from=similar_posts_blogs">«Хтось має виростати у мідлів, а шлях туди стає складнішим». Як штучний інтелект змінює роботу початківців у QA</a></li>
							<li><a href="https://dou.ua/forums/topic/46548/?from=similar_posts_blogs">Коли варто мігрувати на новий automation test framework та як це зробити</a></li>
					</ul>
				</div>


		





		<a name="comments"></a>
		<div class="b-comments ">
				<div id="floatForm" class="hidden-form">
		<div class="b-comments-form __visual-editor">
		<div class="comments-editor-layout">
			<div class="comments-editor-avatar">
					<img class="g-avatar" src="https://s.dou.ua/assets/img/anon.png" width="40" height="40">
			</div>

			<div class="comments-editor-main">
				<div class="textarea-wrap">
					<button
						class="comments-editor-mode-toggle"
						type="button"
						data-comment-editor-mode-toggle
						data-comment-editor-simple-title="Простий режим"
						data-comment-editor-visual-title="Увімкнути редактор"
						title="Простий режим"
						aria-label="Простий режим"
						aria-pressed="false">
						<i class="bi bi-power" aria-hidden="true"></i>
					</button>
					<div
						class="comments-editor-toolbar"
						data-comment-editor-toolbar
						role="toolbar"
						aria-label="Форматування коментаря"
						data-link-prompt="Вставте посилання"
						data-link-fallback-text="текст посилання">
						<button class="comments-editor-button" type="button" data-editor-action="bold" title="Напівжирний (Ctrl+B)" aria-label="Напівжирний">
							<i class="bi bi-type-bold" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="italic" title="Курсив (Ctrl+I)" aria-label="Курсив">
							<i class="bi bi-type-italic" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="strike" title="Перекреслений (Ctrl+Shift+X)" aria-label="Перекреслений">
							<i class="bi bi-type-strikethrough" aria-hidden="true"></i>
						</button>
						<span class="comments-editor-divider" aria-hidden="true"></span>
						<button class="comments-editor-button" type="button" data-editor-action="link" title="Посилання (Ctrl+K)" aria-label="Посилання">
							<i class="bi bi-link-45deg" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="ol" title="Нумерований список (Ctrl+Shift+7)" aria-label="Нумерований список">
							<i class="bi bi-list-ol" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="ul" title="Маркований список (Ctrl+Shift+8)" aria-label="Маркований список">
							<i class="bi bi-list-ul" aria-hidden="true"></i>
						</button>
						<span class="comments-editor-divider" aria-hidden="true"></span>
						<button class="comments-editor-button" type="button" data-editor-action="quote" title="Цитата" aria-label="Цитата">
							<i class="bi bi-blockquote-left" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="code" title="Код" aria-label="Код">
							<i class="bi bi-code-slash" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="pre" title="Блок кода" aria-label="Блок кода">
							<i class="bi bi-code-square" aria-hidden="true"></i>
						</button>
					</div>

					<div class="comments-editor-link-panel" data-comment-editor-link-panel hidden>
						<input
							class="comments-editor-link-input"
							type="text"
							data-comment-editor-link-input
							placeholder="https://">
						<button class="comments-editor-link-action" type="button" data-comment-editor-link-apply>Ок</button>
						<button class="comments-editor-link-action comments-editor-link-action_remove" type="button" data-comment-editor-link-remove>Прибрати</button>
					</div>

					<div
						class="comments-editor-surface b-typo"
						data-comment-editor-surface
						contenteditable="true"
						role="textbox"
						aria-multiline="true"
						data-placeholder="Ваш коментар…"></div>
					<textarea class="first comments-editor-source" data-comment-editor-input aria-hidden="true"></textarea>
				</div>

					<div class="list-tags"><em>Дозволені теги:</em> <span class="formatting-button formatting-button_blockquote">blockquote</span>, a, pre, code, ul, ol, li, b, i, del.</div>

				<div class="send">
					<div class="b-buttons">
						<input class="form-button disabled" type="submit" value="Додати коментар">
							<div class="hint">Ctrl + Enter</div>
						<i class="comment-file-upload bi bi-paperclip"></i>
						<input type="file" class="hiddenFileInput" style="display:none;" accept=".jpg, .jpeg, .png, .gif, .heic" />
						<div class="little-loading"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

			<div class="comments-head" id="fixedableMenuId">
				<div class="fixed-menu">
					<a id="upPageLnkId" class="bi bi-caret-up-fill" title="Вгору" href="javascript:;"></a>
					<h3 id="lblCommentsCount">Немає коментарів</h3>

						<a href="#comments" class="navigation-comment">Додати коментар</a>

					<a id="btnSubscribe" class="comment-subscribe " href="javascript:;"><span class="unchecked-text">Підписатись<span class="m-hide"> на коментарі</span></span><span class="checked-text">Відписатись<span class="m-hide"> від коментарів</span></span></a>




				</div>
				<div class="wrapper"></div>
			</div>

				<div id="inlineForm"><a name="answer"></a>
		<div class="b-comments-form __visual-editor">
		<div class="comments-editor-layout">
			<div class="comments-editor-avatar">
					<img class="g-avatar" src="https://s.dou.ua/assets/img/anon.png" width="40" height="40">
			</div>

			<div class="comments-editor-main">
				<div class="textarea-wrap">
					<button
						class="comments-editor-mode-toggle"
						type="button"
						data-comment-editor-mode-toggle
						data-comment-editor-simple-title="Простий режим"
						data-comment-editor-visual-title="Увімкнути редактор"
						title="Простий режим"
						aria-label="Простий режим"
						aria-pressed="false">
						<i class="bi bi-power" aria-hidden="true"></i>
					</button>
					<div
						class="comments-editor-toolbar"
						data-comment-editor-toolbar
						role="toolbar"
						aria-label="Форматування коментаря"
						data-link-prompt="Вставте посилання"
						data-link-fallback-text="текст посилання">
						<button class="comments-editor-button" type="button" data-editor-action="bold" title="Напівжирний (Ctrl+B)" aria-label="Напівжирний">
							<i class="bi bi-type-bold" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="italic" title="Курсив (Ctrl+I)" aria-label="Курсив">
							<i class="bi bi-type-italic" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="strike" title="Перекреслений (Ctrl+Shift+X)" aria-label="Перекреслений">
							<i class="bi bi-type-strikethrough" aria-hidden="true"></i>
						</button>
						<span class="comments-editor-divider" aria-hidden="true"></span>
						<button class="comments-editor-button" type="button" data-editor-action="link" title="Посилання (Ctrl+K)" aria-label="Посилання">
							<i class="bi bi-link-45deg" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="ol" title="Нумерований список (Ctrl+Shift+7)" aria-label="Нумерований список">
							<i class="bi bi-list-ol" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="ul" title="Маркований список (Ctrl+Shift+8)" aria-label="Маркований список">
							<i class="bi bi-list-ul" aria-hidden="true"></i>
						</button>
						<span class="comments-editor-divider" aria-hidden="true"></span>
						<button class="comments-editor-button" type="button" data-editor-action="quote" title="Цитата" aria-label="Цитата">
							<i class="bi bi-blockquote-left" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="code" title="Код" aria-label="Код">
							<i class="bi bi-code-slash" aria-hidden="true"></i>
						</button>
						<button class="comments-editor-button" type="button" data-editor-action="pre" title="Блок кода" aria-label="Блок кода">
							<i class="bi bi-code-square" aria-hidden="true"></i>
						</button>
					</div>

					<div class="comments-editor-link-panel" data-comment-editor-link-panel hidden>
						<input
							class="comments-editor-link-input"
							type="text"
							data-comment-editor-link-input
							placeholder="https://">
						<button class="comments-editor-link-action" type="button" data-comment-editor-link-apply>Ок</button>
						<button class="comments-editor-link-action comments-editor-link-action_remove" type="button" data-comment-editor-link-remove>Прибрати</button>
					</div>

					<div
						class="comments-editor-surface b-typo"
						data-comment-editor-surface
						contenteditable="true"
						role="textbox"
						aria-multiline="true"
						data-placeholder="Ваш коментар…"></div>
					<textarea class="first comments-editor-source" data-comment-editor-input aria-hidden="true"></textarea>
				</div>

					<div class="list-tags"><em>Дозволені теги:</em> <span class="formatting-button formatting-button_blockquote">blockquote</span>, a, pre, code, ul, ol, li, b, i, del.</div>

				<div class="send">
					<div class="b-buttons">
						<input class="form-button disabled" type="submit" value="