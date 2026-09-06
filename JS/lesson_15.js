// Lesson 15 - асинхронность, Fetch, Promise

// // Пример №1
// console.log("1. Начали");

// setTimeout(() => {
//   console.log("3. Таймер сработал");
// }, 2000);

// console.log("2. Код пошел дальше");

// // Пример №2. Тостер
// console.log("Поставили тостер");

// setTimeout(
//     () => {
//   console.log("Тост готов");
// }, 3000
// );

// Установи таймаут и через N мс, вызови функцию
// setTimeout(
//     функция, миллисекунды
// )

// Создай Promise.
// А внутрь дай мне специальную функцию resolve, которой я потом сообщу: всё, работа завершена успешно.
// resolve можно без проблем переименовать в другое имя. Это просто нразвание

function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
// Promise { <state>: "pending" } - потому что мы явно не долждались завершения :)
// let result = wait(2000)
// console.log("Получим промис", result)

// Первый async \ await
async function makeToast() {
  // Сообщение ДО
  console.log("Поставили тост");

  // Явно дожидаемся результата. (пока ждем - JS может работать в других задачах)
  await wait(3000);
  console.log("Тост готов");
}

makeToast();
console.log("Пока тостер работает я тру салатик");

// ИМИТАЦИЯ СЕТЕВОГО ЗАПРОСА
function fakeFetchEthPrice() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        symbol: "ETH",
        price: 3245,
      });
    }, 2000);
  });
}

async function updateEthPrice() {
  console.log("Запросили новый курс ETH");

  // Дожидаемся ответа "сервера"
  const data = await fakeFetchEthPrice();

  console.log("Ответ получен");
  console.log("Данные", data);
}

updateEthPrice();
console.log("Интерфейс остаётся отзывчивым");

let city = "Усть-Каменогорск";
let apiKey = "23496c2a58b99648af590ee8a29c5348";
let units = "metric";
let lang = "ru";

let finalURL = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=${units}&lang=${lang}`;

async function getWeather() {
  console.log("Запрашиваем погоду...");

  const response = await fetch(finalURL);
  console.log(response); // Promise
  const data = await response.json();
  console.log(response); // JS object с которым можно работать

  console.log("Ответ сервера:");
  console.log(data);

  console.log("Город:", data.name);
  console.log("Температура:", data.main.temp, "°C");
  console.log("Ощущается как:", data.main.feels_like, "°C");
  console.log("Описание:", data.weather[0].description);
}

getWeather();
console.log("Пока погода загружается, JS может выполнять другой код");

// АЛЬТЕРНАТИВНЫЙ ВАРИАНТ С МЕХАНИЗМОМ ПОВТОРА!

// ==========================
// НАСТРОЙКИ
// ==========================

const city = "Усть-Каменогорск";
const apiKey = "23496c2a58b99648af590ee8a29c5348";
const units = "metric";
const lang = "ru";

// Стартовый интервал между повторами
const START_RETRY_DELAY_MS = 1000;

// 3 повтора ПОСЛЕ первой попытки
// Итого максимум будет 4 запроса: 1 основной + 3 retry
const MAX_RETRIES = 3;

const finalURL = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=${units}&lang=${lang}`;

function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function fetchWithRetry(url) {
  const maxAttempts = MAX_RETRIES + 1;

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    const isLastAttempt = attempt === maxAttempts;

    try {
      console.log(`Попытка ${attempt} из ${maxAttempts}`);

      const response = await fetch(url);

      if (response.ok) {
        return response;
      }

      if (isLastAttempt) {
        throw new Error(`Сервер вернул статус ${response.status}`);
      }

      const delayMs = START_RETRY_DELAY_MS * 2 ** (attempt - 1);

      console.log(`Статус ${response.status}. Повтор через ${delayMs} мс...`);

      await wait(delayMs);
    } catch (error) {
      if (isLastAttempt) {
        throw error;
      }

      const delayMs = START_RETRY_DELAY_MS * 2 ** (attempt - 1);

      console.log(`Ошибка запроса: ${error.message}`);
      console.log(`Повтор через ${delayMs} мс...`);

      await wait(delayMs);
    }
  }
}

async function getWeather() {
  try {
    console.log("Запрашиваем погоду...");

    // 1-й await:
    // ждём HTTP-ответ от сервера
    const response = await fetchWithRetry(finalURL);

    console.log("Получили объект Response:");
    console.log(response);

    // 2-й await:
    // читаем body ответа и превращаем JSON в обычный JS-объект
    const data = await response.json();

    console.log("Получили JS-объект с данными:");
    console.log(data);

    console.log("Ответ сервера:");
    console.log("Город:", data.name);
    console.log("Температура:", data.main.temp, "°C");
    console.log("Ощущается как:", data.main.feels_like, "°C");
    console.log("Описание:", data.weather[0].description);
  } catch (error) {
    console.log("Не удалось получить погоду");
    console.log("Причина:", error.message);
  }
}

getWeather();
console.log("Пока погода загружается, JS может выполнять другой код");
