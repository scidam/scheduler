=================================
Регистрационные формы БСИ ДВО РАН 
=================================

.. contents:: :local:


Назначение
----------

Приложение используется для организации быстрой регистрации 
участников на мерояприятия. 
Не предназначено для широкого использования. Является копонентом, дополняющим 
функциональные возможности сайта БСИ ДВО РАН (http://botsad.ru).

Возможности
-----------

- регистрация на определенную дату и время;
- регистрация без учета времени;
- ограничения возможного числа регистрируемых участников за день;
- оповещение участников и кураторов мероприятия по e-mail;
- отмена регистрации по персональной ссылке;

Управление
----------

Управление регистрациями и их просмотр осуществляется через административную панель.
Приложение является многопользовательским. Каждый пользователь может создавать свое расписание с желаемыми
датами проведения регистраций. Также, по желанию, пользователь задает время возможных регистраций и допустимое количество
участников на каждое время\дату. 

Иерархическая модель полномочий пользователей представлена следующими группами:

- группа суперпользователей -- может все без ограничений;
- редакторы регистраций с регулярными правами; могут создавать и редактировать свои личные расписания. не могут вмешиваться в расписания, созданные другими пользователями;
- кураторы регистраций; могут создавать и редактировать расписания любых пользователей;

Чтобы создать новое расписание в Административной панели необходимо нажать вкладку "Добавить Наименование расписания". При этом откроется форма, в которой необходимо будет заполнить поля будущего расписания.

Поля формы "Наименование расписания":

- **Название**. Название расписания используется в теле письма отсылаемом пользователю при оповещении. Оно, например, может быть следующим "Наука в путешествии. ПриМорье.". Тогда, в письме, отсылаемом пользователю при его регистрации, будет отослано: "Здравствуйте, <Имя пользователя>!  Вы успешно зарегистрировались на маршрут "Наука в путешествии. ПриМорье"... 

- **Интервал**, мин. Используется для автоматического назначения времен для всех дат, привязанных к данному расписанию.
- **Начало**. Время начала регистрации для каждой даты. 
- **Конец**. Конец регистрации для каждой даты. 
- **Число участников, max**. Максимальное число участников для каждого времени.  Если предполагается что регистрация осуществляется на день, а не на конкретное время, целесообразно указать здесь достаточно большое число, возможное число участников в день. А уже при редактировании конкретной даты (вкладка "Даты событий") отметить поле "dateonly".

- **User**. Может назначаться только суперпользователем или куратором регистраций. В другом случае, назначается автоматически: указывается имя текущего пользователя, который создает данное расписание. 

Форма "Даты событий" позволяет указать даты, на которые проводится регистрация. Каждая дата должна быть привязана к расписанию.

Поля формы "Даты событий":

- **Расписание**. Выберите из перечня расписание, к которому привязывается дата. Пользователь с регулярными правами редактора регистраций видит только собственные расписания. Суперпользователь и куратор редактора может выбрать любое расписание из имеющихся.
- **Date**. Дата, на которую проводится регистрация. 
- **Dateonly**. Если отмечен, то регистрационная форма, показываемая пользователю, не будет содержать времен для указанной даты. Этим достигается возможность регистрации на день, без указания конкретного времени.

- **Времена регистрации**. Список допустимых времен регистрации. Должен содержать хотя бы одно время (даже в случае, если осуществляется регистрация на день). Времена регистрации могут быть заполнены автоматически для всех созданных дат. Для этого, сначала создаются даты событий, а потом, в перечне расписаний, отмечается галочка около расписания, к которому привязаны даты и выбирается действие "Генерировать расписание" (далее, необходимо нажать "Выполнить"). При нажатии "Выполнить" для всех дат, привязанных к указанному расписанию, создатутся времена, согласно параметрам (Интервал, Начало и Конец из формы "Наименование расписания"). Создавать времена можно и вручную, функциональность генерации времен сделана для удобства. 

Форма "Записи регистраций" заполняется заявками от пользователей. Открывая данную форму можно посмотреть, сколько пользователей зарегистрировалось на каждое мероприятие. Пользователь с регулярными правами редактора видит только пользователей, зарегистрировавшихся на созданные им лично расписания. Куратор регистраций и суперпользователь видит всех зарегистрированных пользователей. 


Процесс регистрации
===================

При регистрации пользователь заполняет микроформу, где указывает свое Имя (оно используется при обращении), номер телефона, e-mail и планируемое число участников. На указанный пользователем e-mail будет направлено письмо о том, что регистрация прошла успешно. В теле письма будет тажке находиться ссылка отмены регистрации. При переходе по этой ссылке созданная регистрационная запись пользователя удаляется. 
Дубликат письма также направлется ответственному за создание данного расписания (если его email адрес был указан). При отмене регистрации, также как и при заполнении регистрационной микроформы, создается оповещение на e-mail.

