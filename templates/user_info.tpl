<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Info</title>
</head>
<body>
    <form action="/submit_signup_form" method="post">
        <h1>User Info Page</h1>

        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required>

        <input type="submit" value="Submit">
    </form>
</body>
</html>