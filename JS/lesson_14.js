console.debug("Файл урока 14 подключен");

// Урок 14 — работа с JSON в JS
//
// ======== ЧТО ТАКОЕ JSON ========
// JSON (JavaScript Object Notation) — текстовый формат обмена данными,
// основанный на синтаксисе объектов JS, но являющийся языконезависимым.
// Он лёгкий для чтения человеком и удобный для машинного парсинга.
//
// Основные правила JSON:
// • Данные хранятся в парах "ключ: значение"
// • Ключи и строки обязательно в ДВОЙНЫХ кавычках
// • Поддерживаемые типы: string, number, object, array, boolean, null
// • Запрещены: функции, undefined, символы, комментарии, одинарные кавычки
//
// Пример валидного JSON:
// {
//   "name": "Анна",
//   "age": 25,
//   "isStudent": false,
//   "courses": ["JS", "HTML", "CSS"],
//   "address": { "city": "Москва", "zip": 101000 }
// }
//
// ======== МЕТОДЫ РАБОТЫ С JSON В JS ========
//
// 1. JSON.stringify(value, replacer?, space?)
//    Преобразует JS-значение (объект, массив и т.д.) в JSON-строку.
//
//    Примеры:
//    const obj = { name: "Иван", age: 30 };
//    const jsonStr = JSON.stringify(obj);
//    // Результат: '{"name":"Иван","age":30}'
//
//    Красивый вывод (с отступами):
//    JSON.stringify(obj, null, 2);
//
//    Фильтрация полей через replacer:
//    JSON.stringify(obj, ["name"]); // только поле name
//
// 2. JSON.parse(text, reviver?)
//    Преобразует JSON-строку обратно в JS-значение (объект/массив).
//
//    Примеры:
//    const jsonStr = '{"name":"Иван","age":30}';
//    const obj = JSON.parse(jsonStr);
//    console.log(obj.name); // "Иван"
//
//    С reviver — функцией для преобразования значений:
//    JSON.parse(jsonStr, (key, value) => key === "age" ? value + 1 : value);
//
// ======== ЧАСТЫЕ ОШИБКИ ========
// • Лишняя запятая в конце массива/объекта — невалидный JSON
// • Одинарные кавычки — невалидный JSON
// • undefined в объекте пропускается, в массиве превращается в null
// • Даты превращаются в ISO-строки при stringify, но НЕ автоматически восстанавливаются при parse
//
// ======== ПОЛЕЗНЫЕ ПАТТЕРНЫ ========
//
// Глубокое клонирование объекта:
// const clone = JSON.parse(JSON.stringify(original));
// (Осторожно: не копирует функции, undefined, Symbol, Date, Map, Set, циклические ссылки)
//
// Работа с localStorage (хранит только строки):
// localStorage.setItem("user", JSON.stringify(userObj));
// const user = JSON.parse(localStorage.getItem("user"));
//
// Асинхетчная загрузка JSON (fetch API):
// fetch("/api/data.json")
//   .then(response => response.json()) // встроенный метод парсинга JSON
//   .then(data => console.log(data));

let wheather =
  '{"coord":{"lon":37.6156,"lat":55.7522},"weather":[{"id":804,"main":"Clouds","description":"пасмурно","icon":"04d"}],"base":"stations","main":{"temp":17.27,"feels_like":16.57,"temp_min":16.86,"temp_max":17.41,"pressure":1020,"humidity":58,"sea_level":1020,"grnd_level":1001},"visibility":10000,"wind":{"speed":4.28,"deg":313,"gust":5.04},"clouds":{"all":100},"dt":1779520114,"sys":{"type":2,"id":2094500,"country":"RU","sunrise":1779498311,"sunset":1779558459},"timezone":10800,"id":524901,"name":"Москва","cod":200}';

// Тут мы полуачем строку, в том виде в котором она придет с сервера
console.log(wheather)

// Тут мы используем инструмент JSON чтобы "спарсить строку json" и превратить ее в JS объект
let wheatherObj = JSON.parse(wheather);

// Тут мы можем работать уже с объектом js
console.log(wheatherObj);
console.log(`Погода в Москве ${wheatherObj.main.temp}`)

let requestObj = {
    city: "Москва",
    type: "current",
    units: "metric",
    lang: "ru",
    userName: undefined,
    userAge: null,
}

let requestJSONString = JSON.stringify(requestObj)
// {"city":"Москва","type":"current","units":"metric","lang":"ru","userAge":null}

console.debug(requestJSONString)

// ======== LOCALSTORAGE, SESSIONSTORAGE, COOKIES ========
//
// --- 1. LOCALSTORAGE ---
// Хранит данные БЕЗСРОЧНО (до явного удаления).
// Объём: ~5-10 МБ.
// Доступ: только из JS, НЕ отправляется на сервер с каждым запросом.
// Использование: тема сайта, настройки пользователя, кэш данных.
//
// localStorage.setItem("key", "value");       // запись
// let data = localStorage.getItem("key");     // чтение (null если нет)
// localStorage.removeItem("key");             // удалить один ключ
// localStorage.clear();                       // очистить всё
// localStorage.length;                        // количество ключей
// localStorage.key(index);                    // получить ключ по индексу
//
// --- 2. SESSIONSTORAGE ---
// Хранит данные только ДО ЗАКРЫТИЯ вкладки/браузера.
// Объём: ~5-10 МБ.
// Доступ: только из JS, НЕ отправляется на сервер, привязан к вкладке.
// Использование: временные данные формы, состояние одной сессии.
//
// Методы идентичны localStorage, только объект — sessionStorage:
// sessionStorage.setItem("key", "value");
// sessionStorage.getItem("key");
// sessionStorage.removeItem("key");
// sessionStorage.clear();
//
// --- 3. COOKIES (документ.cookie) ---
// Хранит данные с возможностью указать СРОК ЖИЗНИ.
// Объём: ~4 КБ (очень мало!).
// Доступ: ЧИТАЕТСЯ и ЗАПИСЫВАЕТСЯ через document.cookie.
// ГЛАВНАЯ ОСОБЕННОСТЬ: отправляется на СЕРВЕР с КАЖДЫМ HTTP-запросом
// (в заголовке Cookie), поэтому не подходит для больших данных.
// Использование: токены авторизации, сессии, tracking, предпочтения языка.
//
// Запись cookie (присваивание НЕ перезаписывает другие cookies!):
// document.cookie = "username=John; expires=Thu, 18 Dec 2025 12:00:00 UTC; path=/; secure; samesite=strict";
//
// Атрибуты при записи:
// • expires=дата  — срок действия (если нет — cookie удалится при закрытии браузера)
// • max-age=сек  — альтернатива expires (число секунд)
// • path=/       — путь, по которому cookie доступен
// • domain=.site.com — для какого домена
// • secure       — передавать только по HTTPS
// • samesite=strict|lax|none — защита от CSRF (strict — самая надёжная)
//
// Чтение всех cookies:
// console.log(document.cookie);
// // "username=John; theme=dark; lang=ru"  (только имя=значение, без атрибутов!)
//
// Удаление cookie — установить expires в прошедшую дату:
// document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
//
// --- СВОДНАЯ ТАБЛИЦА ---
// | Характеристика   | localStorage | sessionStorage | Cookies       |
// |------------------|--------------|----------------|---------------|
// | Объём            | ~5-10 МБ     | ~5-10 МБ       | ~4 КБ         |
// | Срок жизни       | Постоянно    | До закрытия    | Задаётся      |
// | Доступ из JS     | Да           | Да             | Да            |
// | Отправка на сервер| Нет         | Нет            | Да (автомат.)|
// | Привязка         | Домен        | Вкладка        | Домен/путь    |
// | Хранимые типы    | Только строки| Только строки  | Только строки |

// ======== ПРИМЕРЫ РАБОТЫ С ХРАНИЛИЩАМИ ========

// --- ПРИМЕР 1: localStorage (сохранение настроек пользователя) ---
// Когда нужно: запомнить выбор темы, языка, логина и т.д. между визитами.

// Сохраняем настройки:
const userSettings = {
  theme: "dark",
  lang: "ru",
  notifications: true
};

localStorage.setItem("settings", JSON.stringify(userSettings));

// Читаем настройки при загрузке страницы:
let raw = localStorage.getItem("settings");
let settings = raw ? JSON.parse(raw) : { theme: "light", lang: "ru" };
console.log(settings.theme); // "dark"

// Удаляем, если пользователь сбросил настройки:
// localStorage.removeItem("settings");


--- ПРИМЕР 2: sessionStorage (временные данные формы) ---
Когда нужно: сохранить введённое в форму, чтобы не потерять при случайном
обновлении страницы, но не хранить после закрытия вкладки.

При вводе в поле сохраняем значение:
let input = document.getElementById("email");
input.addEventListener("input", () => {
  sessionStorage.setItem("draft_email", input.value);
});

При загрузке страницы восстанавливаем:
let savedEmail = sessionStorage.getItem("draft_email");
if (savedEmail) input.value = savedEmail;

После успешной отправки формы очищаем черновик:
sessionStorage.removeItem("draft_email");


// --- ПРИМЕР 3: Cookies (сессия и авторизация) ---
// Когда нужно: сервер должен узнавать пользователя при каждом запросе
// (например, токен авторизации, ID сессии).

// === Чтение cookies ===
// document.cookie возвращает строку ВСЕХ доступных cookie через точку с запятой.
// Читаем конкретное значение (вручную парсим):
let currentCookies = document.cookie; // "token=abc123; user=Ivan"

function getCookie(name) {
  let cookies = document.cookie;                 // "token=abc123; user=Ivan"
  let cookieArr = cookies.split("; ");            // ["token=abc123", "user=Ivan"]
  
  let found = cookieArr.find(item => item.startsWith(name + "="));
  // find вернёт первую пару, где ключ совпадает с искомым именем
  
  if (!found) return undefined;
  
  return decodeURIComponent(found.split("=")[1]);
  // split("=") делит "token=abc123" на ["token", "abc123"]
  // берём второй элемент (индекс 1) — это значение
}
console.log(getCookie("token")); // "abc123"

// === Установка / обновление cookie ===
// Когда нужно: после успешного логина сервер (или JS) записывает токен,
// чтобы следующие запросы были авторизованными.

document.cookie = "token=abc123; max-age=3600; path=/; secure; samesite=strict";
// token обновлён или создан. Браузер будет отправлять его на сервер 1 час.

// === Удаление cookie ===
// Когда нужно: пользователь нажал "Выйти" — токен надо инвалидировать.

document.cookie = "token=; max-age=0; path=/";
// max-age=0 (или expires в прошлом) моментально удаляет cookie.
// ВАЖНО: path и domain при удалении должны совпадать с теми, что были при создании!