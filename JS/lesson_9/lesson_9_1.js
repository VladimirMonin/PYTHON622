console.debug("9-1 подключен");

const firstName = "Авраам";
const lastName = "Линкольн";

// Типы аргументов в JS у фунцией
// 1. - позиционные аргументы - передаются в определенном порядке, и функция ожидает их в этом порядке
// 2. - Аргументы с дефолтными значениями - если аргумент не передан, то используется значение по умолчанию

// 3 ... - аргументы в виде массива - позволяет передавать неограниченное количество аргументов в виде массива

function sum(a, b){
    return a + b;
}

function getFullName(firstName, lastName = "Петров"){
    return `${firstName} ${lastName}`;
}

console.log("Первый")
console.log("Первый", "Второй", "Третий")

function getMyFriendsNames(...friends){
    // Проверяем тип. friends - массив
    console.debug(friends);
    for (let friend of friends){
        let messageString = `Мой друг - ${friend}`;
        console.debug(messageString);
    }
}






export { firstName, lastName, sum, getFullName, getMyFriendsNames };

