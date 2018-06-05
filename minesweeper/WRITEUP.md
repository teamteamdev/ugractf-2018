# Minesweeper: Write-up

Решение таска «по-честному» предполагает прохождение игры за 5 секунд. Это весьма маловероятно — открытие каждой клетки длится 400 миллисикунд, для победы необходимо открыть все «чистые» клетки, максимальное количество которых — 54 штуки. Таким образом, на открытие всех клеток, в лучшем случае, уходит около 21 секунды.  

Поэтому будем пытаться найти брешь в игре. Внимательно изучаем скрипт, отвечающий за логику страницы. Помимо логики самого сапёра, в конце находится интересная функция:  

```
let sendResults = (score) => {
    let userId = parseInt(getUrlParameter("userId")),
        chatId = parseInt(getUrlParameter("chatId")),
        messageId = parseInt(getUrlParameter("messageId"));
    let url = "/sendresults";
    $.post(url, { userId: userId, score: score, chatId: chatId, messageId: messageId });
};
```

По всей видимости, так Сапёр отправляет результаты игры на сервер для их последующей обработки. Для этого он использует, кроме количества самих очков, `userId`, `messageId` и `chatId`. Можно заметить или интуитивно догадаться по названиям функций, что это GET-параметры, и их значения можно найти в адресной строке. Узнав их, мы можем сами сконструировать POST-запрос к серверу для передачи любого количества очков.

> **TODO**: curl-запрос или что-нибудь такое

Флаг: **ugra_html_games_are_not_secure**