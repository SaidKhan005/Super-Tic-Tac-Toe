# Adding an account functionality
As a user, I would like to have the possibility of having an account, so I could have a more dynamic and engaging experience.

- When I visit the website for the first time, I should have the possibility of creating a new account using a unique username and password.
- For each user who already has an account, should be able to log in on the login/signup page.
- The account should contain the context of each user, that is each account should have:
    - The statistics of the user such as number of games played, number of wins, and total time played 
    - The user's profile
    - Persist ongoing games
    - And any other feature that would be unique for each user

#### Implementation:
- Modify the user and storage architectures to implement an account functionality.
- The user architecture should be capable of retrieving from the database the attributes of the user who is currently logged in.
- The database could implement a function that stores the state of a game, so that if an unfinished game is closed, then that game could be resumed.
- The server would display different values on each page depending on the user who is logged in.