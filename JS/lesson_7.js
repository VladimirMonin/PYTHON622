// Lesson 7 - Объекты в JavaScript
// Объекты - неупорядоченные изменяемые ссылочные коллекции данных, состоящие из пар "ключ-значение". Ключи в объектах являются строками (или символами), а значения могут быть любого типа, включая другие объекты и массивы.

let somePerson = {
  name: "Егор",
  lastName: "Крид",
  age: 30,
  isMarried: false,
  hobbies: ["рекламировать скам", "кидать подписчиков", "петь о любви"],
};

// Доступ к свойствам объекта
console.debug(somePerson.name); // Выведет "Егор"
// console.debug(somePerson["lastName"]); // Выведет "Крид"
console.debug(somePerson.lastName); // Выведет "Крид"

if (somePerson.isMarried) {
  console.debug("Персонаж в браке");
} else {
  console.debug("Персонаж не в браке");
}

console.debug(somePerson.hobbies[0]); // Выведет "рекламировать скам"

// Состарим персонажа на 1 год
somePerson.age = somePerson.age + 1;

// Добавление нового ключа - без проблем!
somePerson.isStudent = false;
console.debug(somePerson);

// Удаление ключа из объекта
delete somePerson.isStudent;
console.debug(somePerson); // Ключ isStudent удален из объекта somePerson

// CRUD - Create, Read, Update, Delete - основные операции с данными, которые можно выполнять с объектами в JavaScript

// Итерация по объекту
// for of - не работает с объектами, так как они не являются итерируемыми коллекциями. Но мы можем использовать for in для итерации по ключам объекта, а затем получать значения по этим ключам внутри цикла. Вот пример:
// Uncaught TypeError: somePerson is not iterable
// for (let someThing of somePerson) {
//   console.debug(someThing); // Это вызовет ошибку, так как somePerson не является итерируемым объектом
// }

someKey = "name";
console.debug(somePerson.someKey); // Выведет undefined - доступ к свойству someKey, которого нет в объекте somePerson
console.debug(somePerson[someKey]); // Выведет "Егор" - доступ к значению по ключу, который хранится в переменной someKey

for (let key in somePerson) {
  console.debug(key);
  console.debug(somePerson[key]);
}

// Проверка теории Михаила - ключи сортируются по алфавиту, а не по порядку добавления
let abvgdeyka = {
  b: "Б",
  a: "А",
  v: "В",
  g: "Г",
  d: "Д",
};
console.debug(abvgdeyka); // Выведет { a: 'А', b: 'Б', d: 'Д', g: 'Г', v: 'В' } - ключи отсортированы по алфавиту, а не по порядку добавления

let lotrPersons = [
  {
    name: "Леголас",
    age: 2931,
    race: "эльф",
    hobbies: ["стрельба из лука", "пение эльфийских песен", "эль"],
  },
  {
    name: "Гимли",
    age: 139,
    race: "гном",
    hobbies: ["ковка оружия", "пение гномьих песен", "гномье не фильтрованое"],
  },
  {
    name: "Арагорн",
    age: 87,
    race: "человек",
    hobbies: [
      "руководство армией",
      "пение человеческих песен",
      "пшеничная на бруньках",
    ],
  },
];

for (let person of lotrPersons) {
  console.debug(`Имя персонажа: ${person.name}`);
  console.debug(`Возраст персонажа: ${person.age}`);
  console.debug(`Раса персонажа: ${person.race}`);
  console.debug(`Хобби персонажа: ${person.hobbies.join(", ")}`);
}

// Работа со свойствами и ключами объектов
// Мы можем получить доступ к служебным коллекциям объекта, таким как Object.keys(), Object.values() и Object.entries(), которые возвращают массивы ключей, значений и пар "ключ-значение" соответственно. Вот пример

// Object.keys() - возвращает массив ключей объекта
// Object.values() - возвращает массив значений объекта
// Object.entries() - возвращает массив пар "ключ-значение" объекта
// Object.fromEntries() - создает объект из массива пар "ключ-значение"

let legolasObject = lotrPersons[0];

let legolasKeys = Object.keys(legolasObject);
console.debug(legolasKeys); // Выведет ["name", "age"...] - массив ключей объекта legolasObject

let legolasValues = Object.values(legolasObject);
console.debug(legolasValues); // Выведет ["Леголас", 2931, "эльф", [...]] - массив значений объекта legolasObject

let legolasEntries = Object.entries(legolasObject);
console.debug(legolasEntries); // Выведет [["name", "Леголас"], ["age", 2931],

for (let value of legolasValues) {
  console.debug(value); // Выведет "Леголас", 2931, "эльф", [...]
}

for (let value of Object.values(legolasObject)) {
  console.debug(value); // Выведет "Леголас", 2931, "эльф", [...]
}

// Деструктуризация массива. Тут это называется оператор spread
// legolasArray на примере
// Spread («распыление») — когда ... распаковывает значения
// Rest («остаток») — когда ... собирает значения в массив/объект

// ЭТО результат Object.entries(legolasObject) - массив пар "ключ-значение" объекта legolasObject
let legolasArray = [
  ["name", "Леголас"],
  ["age", 2931],
  ["race", "эльф"],
  ["hobbies", ["стрельба из лука", "пение эльфийских песен", "эль"]],
];

for (const [key, value] of legolasArray) {
  console.log(`${key}: ${value}`);
}

/////////////////
// Цикл с entries
for (const [key, value] of Object.entries(legolasObject)) {
  console.log(`${key}: ${value}`);
}

// Цикл for in который мы делали в начале
for (const key in legolasObject) {
  console.debug(key);
  console.debug(legolasObject[key]);
}

// Practice - работа с коллекцией фильмов.
// 1. Зайдите в Дипсик или Qwen (что есть с компьютера)
// 2. Введите названия любимых фильмов
// 3. Сделайте следующий запрос:
// Мне нужен массив объектов с данными по этим фильмам в традиционном JS стиле, где каждый объект будет содержать следующие ключи: title, year, genre, director, actors (массив), rating.
// Получите массив не менее 10 позиций
// 4. Выведите в консоль информацию по каждому фильму в формате:
// Название фильма: [title]
// Год выпуска: [year]
// Жанр: [genre]
// Режиссер: [director]
// Актеры: [actors.join(", ")]
// Рейтинг: [rating]

let movies = [
  {
    title: "Матрица",
    year: 1999,
    genre: "Фантастика, Боевик",
    director: "Лана и Лилли Вачовски",
    actors: ["Киану Ривз", "Лоренс Фишберн", "Кэрри-Энн Мосс", "Хьюго Уивинг"],
    rating: 8.7,
  },
  {
    title: "Большой куш",
    year: 2000,
    genre: "Криминал, Комедия",
    director: "Гай Ричи",
    actors: [
      "Брэд Питт",
      "Джейсон Стейтем",
      "Беннисио дель Торо",
      "Деннис Фарино",
    ],
    rating: 8.3,
  },
  {
    title: "Джентльмены",
    year: 2019,
    genre: "Криминал, Боевик, Комедия",
    director: "Гай Ричи",
    actors: ["Мэттью Макконахи", "Чарли Ханнэм", "Хью Грант", "Колин Фаррелл"],
    rating: 7.8,
  },
  {
    title: "Убить Билла",
    year: 2003,
    genre: "Боевик, Триллер",
    director: "Квентин Тарантино",
    actors: ["Ума Турман", "Дэвид Кэррадайн", "Дэррил Ханна", "Люси Лью"],
    rating: 8.2,
  },
  {
    title: "Джанго Освобожденный",
    year: 2012,
    genre: "Вестерн, Драма",
    director: "Квентин Тарантино",
    actors: [
      "Джейми Фокс",
      "Кристоф Вальц",
      "Леонардо ДиКаприо",
      "Кэрри Вашингтон",
    ],
    rating: 8.5,
  },
  {
    title: "Титаник",
    year: 1997,
    genre: "Мелодрама, Драма",
    director: "Джеймс Кэмерон",
    actors: ["Леонардо ДиКаприо", "Кейт Уинслет", "Билли Зейн", "Кэти Бейтс"],
    rating: 7.9,
  },
  {
    title: "Аватар",
    year: 2009,
    genre: "Фантастика, Приключения",
    director: "Джеймс Кэмерон",
    actors: ["Сэм Уортингтон", "Зои Салдана", "Сигурни Уивер", "Стивен Лэнг"],
    rating: 7.9,
  },
  {
    title: "Проект Конец Света",
    year: 2013,
    genre: "Комедия, Фантастика",
    director: "Сет Роген, Эван Голдберг",
    actors: [
      "Джеймс Франко",
      "Сет Роген",
      "Джона Хилл",
      "Дэнни Макбрайд",
      "Эмма Уотсон",
    ],
    rating: 6.6,
  },
  // Дополнительно на мой вкус:
  {
    title: "Побег из Шоушенка",
    year: 1994,
    genre: "Драма",
    director: "Фрэнк Дарабонт",
    actors: ["Тим Роббинс", "Морган Фриман", "Боб Гантон", "Уильям Сэдлер"],
    rating: 9.3,
  },
  {
    title: "Начало",
    year: 2010,
    genre: "Фантастика, Триллер",
    director: "Кристофер Нолан",
    actors: [
      "Леонардо ДиКаприо",
      "Джозеф Гордон-Левитт",
      "Эллиот Пейдж",
      "Том Харди",
    ],
    rating: 8.8,
  },
  {
    title: "Бойцовский клуб",
    year: 1999,
    genre: "Триллер, Драма",
    director: "Дэвид Финчер",
    actors: ["Брэд Питт", "Эдвард Нортон", "Хелена Бонем Картер", "Мит Лоаф"],
    rating: 8.8,
  },
];

// 4. Выведите в консоль информацию по каждому фильму в формате:
// Название фильма: [title]
// Год выпуска: [year]
// Жанр: [genre]
// Режиссер: [director]
// Актеры: [actors.join(", ")]
// Рейтинг: [rating]

for (let movie of movies) {
    console.debug(`------------------------------`);
    console.debug(`Название фильма: ${movie.title}`);
    console.debug(`Год выпуска: ${movie.year}`);
    console.debug(`Жанр: ${movie.genre}`);
    console.debug(`Режиссер: ${movie.director}`);
    console.debug(`Актеры: ${movie.actors.join(", ")}`);
    console.debug(`Рейтинг: ${movie.rating}`);
    // СОЗДАТЬ КАРТОЧКУ
}