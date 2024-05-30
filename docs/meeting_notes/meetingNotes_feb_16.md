## Meeting Notes

**SCRUM Master:** Flavio Cesar Mendoza Trinidad
**Recorded by:**  Said Khan
**Notes submitted on:** 16/02/2024  
**Venue:** EN 1054 Classroom  
**Source:** None   
**Time:** 2:00PM - 2:50PM  
**Attendance:** Kaleb, Flavio, Mohammad, Said, Christopher

Agenda:

- Collection of UML Diagram - 
Every team member is required to have a UML diagram posted by the end of the day
The UML diagrams will be combined into one by the 17th of Febuary


- Deadline for merging requests: Saturday 17 - 
Every team member must finish their part of the project so that the person in charge of the merge requests
is able to review the codes and merge every branch into the master.


- Kaleb will be the person in charge of the merge requests.


- We got a better understanding with Program flow. It has been outlined below:

### Program flow:
We decided to go with an object oriented approach.

1) The server will require 4 templates for now. The user_info, next_page, winner and draw template. 
2) we agreed the server will pass a list of dictionaries containing user info to the user module
3) The user module will create the two users and pass these objects to the game module. We agreed to use user_name as the id for now.
4) The game module will create a game instance containing the two user objects. Hence, each new game would be a completely new game object instance.

    
   This will allow the server and storage module to maintain communication through via the game module hence reducing coupling  
    There will be an addition of a non random game id varaiable.
