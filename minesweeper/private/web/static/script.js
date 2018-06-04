$(document).ready(() => {

    let body = $("body"),
        startPage = $("#start-page"),
        gamePage = $("#game-page"),
        resultPage = $("#result-page"),
        table = $("#grid"),
        timer = $("#timer"),
        grid = [],
        cellStates = [],
        cells = [],
        bombsCount = 0,
        isFieldInited = false,
        isGameEnded = false,
        time = 0,
        timerIntervalId,
        longClickTimer,
        timed = false,
        clearCellsCount = 0;
    const sizeX = 8,
        sizeY = 8,
        maxBombs = 10;

    gamePage.hide();
    resultPage.hide();

    // initialization

    let create = () => {
        for (let i = 0; i < sizeX; i++) {
            let tr = $("<tr></tr>"),
                cellRow = [],
                gridRow = [],
                cellStatesRow = [];
            for (let j = 0; j < sizeY; j++) {
                let cell = $('<td class="cell"></td>');
                cell.on("click", () => {
                    if (timed) {
                        clearTimeout(longClickTimer);
                        console.log("yeah");
                        timed = false;
                        flagCell(cell, i, j);
                    } else {
                        longClickTimer = setTimeout(() => {
                            timed = false;
                            openCell(cell, i, j);
                        }, 200);
                        timed = true;
                    }
                });
                cellRow.push(cell);
                tr.append(cell);
                gridRow.push(0);
                cellStatesRow.push(0);
            }
            table.append(tr);
            cells.push(cellRow);
            grid.push(gridRow);
            cellStates.push(cellStatesRow);
        }
    };

    let initializeGameField = (openedX, openedY) => {
        for (let i = 0; i < sizeX; i++) {
            for (let j = 0; j < sizeY; j++) {
                if (Math.random() <= 0.2 && bombsCount < maxBombs && !(i === openedX && j === openedY)) {
                    grid[i][j] = 9;
                    bombsCount += 1;
                    for (let i1 = i - 1; i1 < i + 2; i1++) {
                        for (let j1 = j - 1; j1 < j + 2; j1++) {
                            if (checkCell(i1, j1)) {
                                grid[i1][j1] += 1;
                            }
                        }
                    }
                } else {
                    clearCellsCount += 1;
                }
            }
        }
        isFieldInited = true;
        timerIntervalId = setInterval(timeCounter, 1000);
    };

    let openCell = (cell, x, y) => {
        if (checkCell(x, y)) {
            if (!isFieldInited) {
                initializeGameField(x, y);
            }
            cell.attr("class", "opened");
            if (grid[x][y] < 9) {
                clearCellsCount -= 1;
                if (clearCellsCount === 0 && !isGameEnded) {
                    winGame();
                }
                cellStates[x][y] = 1;
                adjustColor(cell, grid[x][y]);
                if (grid[x][y] === 0) {
                    for (let i = x - 1; i < x + 2; i++) {
                        for (let j = y - 1; j < y + 2; j++) {
                            if (checkCell(i, j)) {
                                openCell(cells[i][j], i, j);
                            }
                        }
                    }
                } else {
                    cell.html(grid[x][y]);
                }
            } else {
                cell.html('💣');
                cell.css("color", "red");
                if (!isGameEnded) {
                    loseGame();
                }
            }
        }
    };

    let flagCell = (cell, x, y) => {
        if (cellStates[x][y] === 0 && !isGameEnded) {
            cell.html('⛳');
            cell.css("color", "white");
            cellStates[x][y] = 2;
        } else if (cellStates[x][y] === 2 && !isGameEnded) {
            cell.empty();
            cellStates[x][y] = 0;
        }
    };

    let checkCell = (x, y) => {
        if (x >= 0 && x < sizeX && y >= 0 && y < sizeY) {
            if (cellStates[x][y] === 0 || (cellStates[x][y] === 2 && isGameEnded)) {
                return true;
            }
        }
        return false;
    };

    let adjustColor = (cell, number) => {
        if (number === 1) {
            cell.css("color", "blue");
        } else if (number === 2) {
            cell.css("color", "green");
        } else if (number === 3) {
            cell.css("color", "red");
        } else if (number === 4) {
            cell.css("color", "darkblue");
        } else if (number === 5) {
            cell.css("color", "darkred");
        } else if (number === 6) {
            cell.css("color", "#4166F5")
        } else if (number === 7) {
            cell.css("color", "black");
        } else if (number === 8) {
            cell.css("color", "grey");
        }
    };

    let timeCounter = () => {
        if (!isGameEnded) {
            time++;
            let minutes = `${Math.floor(time / 60)}`;
            let strMinutes = minutes >= 10 ? minutes.toString() : '0' + minutes.toString();
            let seconds = `${time - Math.floor(time / 60) * 60}`;
            let strSeconds = seconds >= 10 ? seconds.toString() : '0' + seconds.toString();
            timer.html(`${strMinutes}:${strSeconds}`);
        }
    };

    let loseGame = () => {
        isGameEnded = true;
        for (let i = 0; i < sizeX; i++) {
            for (let j = 0; j < sizeY; j++) {
                openCell(cells[i][j], i, j);
            }
        }
        clearInterval(timerIntervalId);
    };

    let winGame = () => {
        isGameEnded = true;
        clearInterval(timerIntervalId);
        let score = Math.round(1000 / time);
        sendResults(score);
        gamePage.fadeOut(200, () => {
            $("#result-time").html(`You won! Your time: ${timer.html()}`);
            $("#result-score").html(`Score: ${score}`);
            resultPage.fadeIn(200);
        })
    };

    $("#start").on("click", () => {
        startPage.fadeOut(100, () => {
            gamePage.fadeIn(100);
        });
    });

    $(".restart").on("click", () => {
        resultPage.fadeOut(200);
        gamePage.fadeOut(200, () => {
            table.empty();
            grid = [];
            cellStates = [];
            cells = [];
            bombsCount = 0;
            isGameEnded = false;
            isFieldInited = false;
            time = 0;
            clearCellsCount = 0;
            timer.html("00:00");
            create();
            gamePage.fadeIn(200);
        });
    });

    let getUrlParameter = (parameterName) => {
        let pageUrl = decodeURIComponent(window.location.search.substring(1)),
            urlVars = pageUrl.split('&');
        for (let i = 0; i < urlVars.length; i++) {
            let param = urlVars[i].split('=');
            if (param[0] === parameterName) {
                return param[1];
            }
        }
        return undefined;
    };

    let sendResults = (score) => {
        let userId = parseInt(getUrlParameter("userId")),
            chatId = parseInt(getUrlParameter("chatId")),
            messageId = parseInt(getUrlParameter("messageId"));
        let url = "/post/";
        $.post(url, { userId: userId, score: score, chatId: chatId, messageId: messageId });
    };

    create();
});
