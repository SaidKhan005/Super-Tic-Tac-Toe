Project Description COMP2005, Fall 2024

The term project is a simple two player game server. The initial game to include with this server is commonly called 
"super tic tac toe" or "ultimate tic tac toe". You can easily find examples of the game online and even sample 
implementations on code repositories such as GitHub for inspiration.

In order to keep this from being a project of simply copying other people's code, there are a few things to keep in mind:
* Most of the grades in the project will be focussed on application of demonstration of software engineering techniques 
and practice, including code design, architecture, and techniques for teamwork. It is assumed you can get your code 
working, and the focus of the course is not programming, so that is not where most of the course evaluation lies.
* You will be expected to introduce some original features in your project in later stages, so there is no point in 
incorporating code you do not understand into the project. 

You are expected to create a python-based WSGI server, using the URL endpoint routing provided by the Bottle web 
framework.

Here is some functionality you will need to implement:

* Player registration
* Adding players to a game
* Starting up a new game
* Logging into a game
* Making a move in a game
* Checking if the other player has moved
* Determining the end of a game
* Persisting games between user sessions

Here is some functionality you may decide to implement:
* Tracking a player's performance
* Issuing of challenges between players
* Holding tournaments with leader boards (with additional tournament features)
* Game playback
* Time limits on player moves 
* Synchronous and asynchronous game play

More possible features of the project will be generated by your team as the project progresses.
