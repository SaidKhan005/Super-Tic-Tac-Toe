<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic Tac Toe Board</title>
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

        .current-player {
            color: #4CAF50; /* Highlight the current player with a different color */
        }
    </style>

</head>
<body>
    <h1>Loaded Game Information</h1>
    <p><strong>Game ID:</strong> {{ game_info.get('game_id') }}</p>
    <p><strong>Players:</strong> {{ game_info.get('player1') }} vs {{ game_info.get('player2') }}</p>
    <p><strong>Number of Moves:</strong> {{ game_info.get('num_of_moves') }}</p>
    <p><strong>Winner:</strong> {{ game_info.get('winner')}}</p>
    <h2>Game Matrix</h2>
    <div class="container">
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][0][0]}}</td>
                    <td>{{game_info['matrix'][0][1]}}</td>
                    <td>{{game_info['matrix'][0][2]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][1][0]}}</td>
                    <td>{{game_info['matrix'][1][1]}}</td>
                    <td>{{game_info['matrix'][1][2]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][2][0]}}</td>
                    <td>{{game_info['matrix'][2][1]}}</td>
                    <td>{{game_info['matrix'][2][2]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][0][3]}}</td>
                    <td>{{game_info['matrix'][0][4]}}</td>
                    <td>{{game_info['matrix'][0][5]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][1][3]}}</td>
                    <td>{{game_info['matrix'][1][4]}}</td>
                    <td>{{game_info['matrix'][1][5]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][2][3]}}</td>
                    <td>{{game_info['matrix'][2][4]}}</td>
                    <td>{{game_info['matrix'][2][5]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                     <td>{{game_info['matrix'][0][6]}}</td>
                     <td>{{game_info['matrix'][0][7]}}</td>
                     <td>{{game_info['matrix'][0][8]}}</td>
                </tr>
                <tr>
                     <td>{{game_info['matrix'][1][6]}}</td>
                     <td>{{game_info['matrix'][1][7]}}</td>
                     <td>{{game_info['matrix'][1][8]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][2][6]}}</td>
                    <td>{{game_info['matrix'][2][7]}}</td>
                    <td>{{game_info['matrix'][2][8]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][3][0]}}</td>
                    <td>{{game_info['matrix'][3][1]}}</td>
                    <td>{{game_info['matrix'][3][2]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][4][0]}}</td>
                    <td>{{game_info['matrix'][4][1]}}</td>
                    <td>{{game_info['matrix'][4][2]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][5][0]}}</td>
                    <td>{{game_info['matrix'][5][1]}}</td>
                    <td>{{game_info['matrix'][5][2]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][3][3]}}</td>
                    <td>{{game_info['matrix'][3][4]}}</td>
                    <td>{{game_info['matrix'][3][5]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][4][3]}}</td>
                    <td>{{game_info['matrix'][4][4]}}</td>
                    <td>{{game_info['matrix'][4][5]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][5][3]}}</td>
                    <td>{{game_info['matrix'][5][4]}}</td>
                    <td>{{game_info['matrix'][5][5]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                   <td>{{game_info['matrix'][3][6]}}</td>
                    <td>{{game_info['matrix'][3][7]}}</td>
                    <td>{{game_info['matrix'][3][8]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][4][6]}}</td>
                    <td>{{game_info['matrix'][4][7]}}</td>
                    <td>{{game_info['matrix'][4][8]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][5][6]}}</td>
                    <td>{{game_info['matrix'][5][7]}}</td>
                    <td>{{game_info['matrix'][5][8]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][6][0]}}</td>
                    <td>{{game_info['matrix'][6][1]}}</td>
                    <td>{{game_info['matrix'][6][2]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][7][0]}}</td>
                    <td>{{game_info['matrix'][7][1]}}</td>
                    <td>{{game_info['matrix'][7][2]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][8][0]}}</td>
                    <td>{{game_info['matrix'][8][1]}}</td>
                    <td>{{game_info['matrix'][8][2]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][6][3]}}</td>
                    <td>{{game_info['matrix'][6][4]}}</td>
                    <td>{{game_info['matrix'][6][5]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][7][3]}}</td>
                    <td>{{game_info['matrix'][7][4]}}</td>
                    <td>{{game_info['matrix'][7][5]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][8][3]}}</td>
                    <td>{{game_info['matrix'][8][4]}}</td>
                    <td>{{game_info['matrix'][8][5]}}</td>
                </tr>
            </table>
        </div>
        <div class="board">
            <table class="game-board">
                <tr>
                    <td>{{game_info['matrix'][6][6]}}</td>
                    <td>{{game_info['matrix'][6][7]}}</td>
                    <td>{{game_info['matrix'][6][8]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][7][6]}}</td>
                    <td>{{game_info['matrix'][7][7]}}</td>
                    <td>{{game_info['matrix'][7][8]}}</td>
                </tr>
                <tr>
                    <td>{{game_info['matrix'][8][6]}}</td>
                    <td>{{game_info['matrix'][8][7]}}</td>
                    <td>{{game_info['matrix'][8][8]}}</td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>
