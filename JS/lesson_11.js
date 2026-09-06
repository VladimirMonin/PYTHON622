console.debug("Файл lesson_11.js подключен");

// DOM - Document Object Model - это объектная модель документа, которая позволяет нам взаимодействовать с HTML-документом через JavaScript.

// Получаем ВЕСЬ ОБЪЕКТ. Обычно так не делают)
console.debug(document);

// Методы для получения элементов из документа:
// 1. getElementById - получает элемент по его id
// 2. querySelector - получает первый элемент, который соответствует CSS-селектору
// 3. querySelectorAll - получает все элементы, которые соответствуют CSS-селектору

// Получаем элемент по тегу
// h1 - селектор по тегу. .class-name - селектор по классу. #id-name - селектор по id
const h1 = document.querySelector("h1");
console.debug(h1);

// Самые популярные поля элемента:
// 1. TextContent - текстовое содержимое элемента
// 2. InnerHTML - HTML-содержимое элемента
// 3. ClassList - список классов элемента
// 4. OuterHTML - HTML-содержимое элемента, включая сам элемент

// Получаем текстовое содержимое элемента
console.debug(h1.textContent);

// Меняем текстовое содержимое элемента
h1.textContent = "Урок 11. DOM. Изменили текст заголовка";

// Получаем список классов элемента
console.debug(h1.classList);

// Добавляем класс элементу
h1.classList.add("red-text");

// Создаем новые элемент UL
// createElement - создает новый элемент с указанным тегом
const ul = document.createElement("ul");

// Добавляем элемент UL в body
// document.body - получает элемент body
// appendChild - добавляет элемент в конец списка дочерних элементов
document.body.appendChild(ul);

// while (true) {
//   const li = document.createElement("li");
//   const text = prompt(
//     "Введите текст для элемента списка (или 'stop' для остановки)",
//   );
//   if (text === "stop") {
//     break;
//   }
//   li.textContent = text;
//   ul.appendChild(li);
// }

const students = [
  {
    surname: "Абдукодиров",
    name: "Жавохир",
    patronymic: "Фарход Угли",
  },
  {
    surname: "Анищенко",
    name: "Валентина",
    patronymic: "Александровна",
  },
  {
    surname: "Афанасьев",
    name: "Никита",
    patronymic: "Юрьевич",
  },
  {
    surname: "Венин",
    name: "Владислав",
    patronymic: "Сергеевич",
  },
  {
    surname: "Герасимов",
    name: "Никита",
    patronymic: "Сергеевич",
  },
  {
    surname: "Гудков",
    name: "Евгений",
    patronymic: "Олегович",
  },
  {
    surname: "Дацій",
    name: "Александр",
    patronymic: "Вадимирович",
  },
  {
    surname: "Денисова",
    name: "Ирина",
    patronymic: "Владимировна",
  },
  {
    surname: "Дрягин",
    name: "Антон",
    patronymic: "Константинович",
  },
  {
    surname: "Зверьков",
    name: "Михаил",
    patronymic: "Вячеславович",
  },
  {
    surname: "Истомин",
    name: "Степан",
    patronymic: "Алексеевич",
  },
  {
    surname: "Казанцев",
    name: "Михаил",
    patronymic: "Романович",
  },
  {
    surname: "Котова",
    name: "Виктория",
    patronymic: "Романовна",
  },
  {
    surname: "Наседкин",
    name: "Валентин",
    patronymic: "Сергеевич",
  },
  {
    surname: "Наседкина",
    name: "Алина",
    patronymic: "Жумагуловна",
  },
  {
    surname: "Овсепян",
    name: "Тагуи",
    patronymic: "Амбарцумовна",
  },
  {
    surname: "Одинцов",
    name: "Роман",
    patronymic: "Сергеевич",
  },
  {
    surname: "Рыльская",
    name: "Елена",
    patronymic: "Святославовна",
  },
  {
    surname: "Троянский",
    name: "Данил",
    patronymic: "Александрович",
  },
  {
    surname: "Халявин",
    name: "Арсений",
    patronymic: "Андреевич",
  },
  {
    surname: "Чередилина",
    name: "Анастасия",
    patronymic: "Игоревна",
  },
  {
    surname: "Шаповал",
    name: "Владимир",
    patronymic: "Павлович",
  },
];

// 1. Найти таблицу по id
const table = document.getElementById("group-table");

// 2. Создать массив заголовков таблицы
const headers = ["Фамилия", "Имя", "Отчество"];

// 3. Создать строку заголовков и добавить ее в таблицу
const headerRow = document.createElement("tr");

// 4. Берем заголовки и под каждый создаем новый элемент th и добавляем его в строку заголовков
headers.forEach((header) => {
  const th = document.createElement("th");
  th.textContent = header;
  headerRow.appendChild(th);
});

// 5. Добавляем строку заголовков в таблицу
table.appendChild(headerRow);

// 6. Проходим по массиву студентов и для каждого студента создаем строку таблицы
students.forEach((student) => {
  //   Создание строки и ячеек
  const row = document.createElement("tr");
  const surnameCell = document.createElement("td");
  const nameCell = document.createElement("td");
  const patronymicCell = document.createElement("td");
  //   Заполнение тегов ячеек данными из объекта студента
  surnameCell.textContent = student.surname;
  nameCell.textContent = student.name;
  patronymicCell.textContent = student.patronymic;
  //   Добавление ячеек в строку
  row.appendChild(surnameCell);
  row.appendChild(nameCell);
  row.appendChild(patronymicCell);
  //   Добавление строки в таблицу
  table.appendChild(row);
});

function filterStudents() {
    // 1. Вызвать промпт - получить поисковую строку
    // 2. Отфильтровать исходный массив студентов через метод filter и стрелку
    // 3. table.innerHTML = "" - очистить таблицу от старых данных"
    // 4. Отрисовывыаем новые данные
}

// Функции?
// 1. Отрисовки студентов
// 2. Функция создания табличной строки (массив на входе или ...)
// 3. Функция фильтрации студентов (по фамилии, имени, отчеству)