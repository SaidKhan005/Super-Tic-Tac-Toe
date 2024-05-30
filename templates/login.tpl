<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
        }

        h2 {
            font-size: 2em;
            color: #333;
            margin-top: 50px;
        }

        form {
            margin-top: 20px;
        }

        input[type="text"] {
            padding: 10px;
            margin: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 200px;
            font-size: 16px;
        }

        .btn {
            padding: 10px 20px;
            font-size: 1.2em;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #45a049;
        }

        .create-user-link {
            font-size: 14px;
            color: #333;
            text-decoration: none;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h2>Login</h2>
    <form action="/start_game" method="post">
        <input type="text" name="username1" placeholder="Enter User 1 Username" required><br>
        <input type="text" name="username2" placeholder="Enter User 2 Username" required><br>
        <input type="submit" class="btn" value="Start Game"><br>
    </form>
    <a href="/sign_up" class="create-user-link">Create User</a>
</body>
</html>
