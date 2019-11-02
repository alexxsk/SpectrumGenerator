# EDEM task 1

__Симуляція (моделювання) апаратурного спектру__
_1. Задати з файлу (чи за вибором викладача в програмі):_
- лінії, які будуть присутні в спектрі (їх характеристики – енергія, інтенсивність, ширина на половині висоти ΔE в апаратурному спектрі). В файлі необхідно забезпечити написання коментарів у будь-якому рядку, а також значення змінних не повинні прив’язуватися до номеру рядку. На всі
змінні повинні бути коментарі – що це, і можливий діапазон зміни значень. Ліній можна задавати необмежену кількість.
- Задати параметри фону: складається із суми спадаючої експоненти та лінійного фону (2 + 2 параметри).
- Задати вхідний досліджуваний енергетичний діапазон (від 0 до Emax), кількість каналів спектру та початковий зсув (E0 при нульовому номері каналу).

_2. Сформувати (також може виводиться зображення на кожному етапі – задається у конфігураційному файлі, як і в п.1):_
- Вхідний (фізичний) спектр без фону і без уширення піків (також виводиться зображення)
- Вхідний (фізичний) спектр з фоном без уширення піків (також виводиться зображення)
- Апаратурний спектр з фоном з уширенням піків без статистичного розкиду в каналах. Уширення проводити за такими алгоритмами (опціональний вибір через вхідні параметри – не програміста, а викладача чи користувача)
  - ΔE використовується із даних 1 пункту
  - ΔE = a0 + a1\*sqrt(E) (поясніть, чому використовують таку залежність), a0, a1 – параметри.

- Апаратурний спектр з фоном з уширенням піків із статистичним розкидом в каналах:
  - згідно закону Пуассона;
  - при значеннях в каналі менше 10 розкид згідно закону Пуассона, при значеннях більше 10 апроксимувати гауссівським наближенням із sigma = sqrt(N) , де N – кількість відліків в каналі.

_3. Вивести спектри, сформовані в попередньому пункті в файл і в графічному
вигляді._
_4. Протестувати та проаналізувати отримані результати (варіюючи параметри і
досліджуючи результуючі спектри)._
_5. Вивести залежність sigma від ΔE (FWHM, ПШПВ) для розподілу Гаусса (необхідне при симуляції)._
