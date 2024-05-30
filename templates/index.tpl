<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic Tac Toe</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            width: 600px;
            margin: 0 auto;
        }

        .board {
            width: 30%;
            margin-bottom: 20px;
            border: 2px solid #000;
        }

        .game-board {
            width: 100%;
            border-collapse: collapse;
        }

        .game-board td {
            width: 33.33%;
            height: 50px;
            border: 1px solid #000;
            text-align: center;
            font-size: 24px;
            cursor: pointer;
        }

        a {
            text-decoration: none;
            color: #333;
        }

        .current-player {
            color: #4CAF50; /* Highlight the current player with a different color */
        }
    </style>

    <script>
        function makeMove(row, col) {
            fetch(`/make_move/${row}/${col}`, {
                method: 'POST'
            })
            .then(response => response.text())
            .then(data => {
                document.body.innerHTML = data;
            });
        }
    </script>
</head>
<body>
    <h1>Tic Tac Toe</h1>
    <p><strong>Game ID:</strong> {{game_id }}</p>
    <p>Current turn: <span class="current-player">{{current_player}}</span></p>
    <div class="container">
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(0, 0)"><a href="#">{{board[0][0]}}</a></td>
                    <td onclick="makeMove(0, 1)"><a href="#">{{board[0][1]}}</a></td>
                    <td onclick="makeMove(0, 2)"><a href="#">{{board[0][2]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(1, 0)"><a href="#">{{board[1][0]}}</a></td>
                    <td onclick="makeMove(1, 1)"><a href="#">{{board[1][1]}}</a></td>
                    <td onclick="makeMove(1, 2)"><a href="#">{{board[1][2]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(2, 0)"><a href="#">{{board[2][0]}}</a></td>
                    <td onclick="makeMove(2, 1)"><a href="#">{{board[2][1]}}</a></td>
                    <td onclick="makeMove(2, 2)"><a href="#">{{board[2][2]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(0, 3)"><a href="#">{{board[0][3]}}</a></td>
                    <td onclick="makeMove(0, 4)"><a href="#">{{board[0][4]}}</a></td>
                    <td onclick="makeMove(0, 5)"><a href="#">{{board[0][5]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(1, 3)"><a href="#">{{board[1][3]}}</a></td>
                    <td onclick="makeMove(1, 4)"><a href="#">{{board[1][4]}}</a></td>
                    <td onclick="makeMove(1, 5)"><a href="#">{{board[1][5]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(2, 3)"><a href="#">{{board[2][3]}}</a></td>
                    <td onclick="makeMove(2, 4)"><a href="#">{{board[2][4]}}</a></td>
                    <td onclick="makeMove(2, 5)"><a href="#">{{board[2][5]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(0, 6)"><a href="#">{{board[0][6]}}</a></td>
                    <td onclick="makeMove(0, 7)"><a href="#">{{board[0][7]}}</a></td>
                    <td onclick="makeMove(0, 8)"><a href="#">{{board[0][8]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(1, 6)"><a href="#">{{board[1][6]}}</a></td>
                    <td onclick="makeMove(1, 7)"><a href="#">{{board[1][7]}}</a></td>
                    <td onclick="makeMove(1, 8)"><a href="#">{{board[1][8]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(2, 6)"><a href="#">{{board[2][6]}}</a></td>
                    <td onclick="makeMove(2, 7)"><a href="#">{{board[2][7]}}</a></td>
                    <td onclick="makeMove(2, 8)"><a href="#">{{board[2][8]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(3, 0)"><a href="#">{{board[3][0]}}</a></td>
                    <td onclick="makeMove(3, 1)"><a href="#">{{board[3][1]}}</a></td>
                    <td onclick="makeMove(3, 2)"><a href="#">{{board[3][2]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(4, 0)"><a href="#">{{board[4][0]}}</a></td>
                    <td onclick="makeMove(4, 1)"><a href="#">{{board[4][1]}}</a></td>
                    <td onclick="makeMove(4, 2)"><a href="#">{{board[4][2]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(5, 0)"><a href="#">{{board[5][0]}}</a></td>
                    <td onclick="makeMove(5, 1)"><a href="#">{{board[5][1]}}</a></td>
                    <td onclick="makeMove(5, 2)"><a href="#">{{board[5][2]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(3, 3)"><a href="#">{{board[3][3]}}</a></td>
                    <td onclick="makeMove(3, 4)"><a href="#">{{board[3][4]}}</a></td>
                    <td onclick="makeMove(3, 5)"><a href="#">{{board[3][5]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(4, 3)"><a href="#">{{board[4][3]}}</a></td>
                    <td onclick="makeMove(4, 4)"><a href="#">{{board[4][4]}}</a></td>
                    <td onclick="makeMove(4, 5)"><a href="#">{{board[4][5]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(5, 3)"><a href="#">{{board[5][3]}}</a></td>
                    <td onclick="makeMove(5, 4)"><a href="#">{{board[5][4]}}</a></td>
                    <td onclick="makeMove(5, 5)"><a href="#">{{board[5][5]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(3, 6)"><a href="#">{{board[3][6]}}</a></td>
                    <td onclick="makeMove(3, 7)"><a href="#">{{board[3][7]}}</a></td>
                    <td onclick="makeMove(3, 8)"><a href="#">{{board[3][8]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(4, 6)"><a href="#">{{board[4][6]}}</a></td>
                    <td onclick="makeMove(4, 7)"><a href="#">{{board[4][7]}}</a></td>
                    <td onclick="makeMove(4, 8)"><a href="#">{{board[4][8]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(5, 6)"><a href="#">{{board[5][6]}}</a></td>
                    <td onclick="makeMove(5, 7)"><a href="#">{{board[5][7]}}</a></td>
                    <td onclick="makeMove(5, 8)"><a href="#">{{board[5][8]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(6, 0)"><a href="#">{{board[6][0]}}</a></td>
                    <td onclick="makeMove(6, 1)"><a href="#">{{board[6][1]}}</a></td>
                    <td onclick="makeMove(6, 2)"><a href="#">{{board[6][2]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(7, 0)"><a href="#">{{board[7][0]}}</a></td>
                    <td onclick="makeMove(7, 1)"><a href="#">{{board[7][1]}}</a></td>
                    <td onclick="makeMove(7, 2)"><a href="#">{{board[7][2]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(8, 0)"><a href="#">{{board[8][0]}}</a></td>
                    <td onclick="makeMove(8, 1)"><a href="#">{{board[8][1]}}</a></td>
                    <td onclick="makeMove(8, 2)"><a href="#">{{board[8][2]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(6, 3)"><a href="#">{{board[6][3]}}</a></td>
                    <td onclick="makeMove(6, 4)"><a href="#">{{board[6][4]}}</a></td>
                    <td onclick="makeMove(6, 5)"><a href="#">{{board[6][5]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(7, 3)"><a href="#">{{board[7][3]}}</a></td>
                    <td onclick="makeMove(7, 4)"><a href="#">{{board[7][4]}}</a></td>
                    <td onclick="makeMove(7, 5)"><a href="#">{{board[7][5]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(8, 3)"><a href="#">{{board[8][3]}}</a></td>
                    <td onclick="makeMove(8, 4)"><a href="#">{{board[8][4]}}</a></td>
                    <td onclick="makeMove(8, 5)"><a href="#">{{board[8][5]}}</a></td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td onclick="makeMove(6, 6)"><a href="#">{{board[6][6]}}</a></td>
                    <td onclick="makeMove(6, 7)"><a href="#">{{board[6][7]}}</a></td>
                    <td onclick="makeMove(6, 8)"><a href="#">{{board[6][8]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(7, 6)"><a href="#">{{board[7][6]}}</a></td>
                    <td onclick="makeMove(7, 7)"><a href="#">{{board[7][7]}}</a></td>
                    <td onclick="makeMove(7, 8)"><a href="#">{{board[7][8]}}</a></td>
                </tr>
                <tr>
                    <td onclick="makeMove(8, 6)"><a href="#">{{board[8][6]}}</a></td>
                    <td onclick="makeMove(8, 7)"><a href="#">{{board[8][7]}}</a></td>
                    <td onclick="makeMove(8, 8)"><a href="#">{{board[8][8]}}</a></td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>