# Super Tic Tac Toe Web Game

## Overview

This project is a web-based implementation of the Super Tic Tac Toe game. It allows users to play the game online through a web browser. The game features player registration, starting new games, making moves, and determining the winner.

## Installation

To run this project, you need to have Python installed on your system. If you don't have Python installed, you can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

Once you have Python installed, you can install the Bottle framework using pip, the Python package manager. Open a terminal or command prompt and run the following command:

pip install bottle

This will install the Bottle framework and its dependencies on your system. After installing Bottle, you're ready to run the project.

## Usage

To start the server and play the game, run the following command:

python server.py

Then, open your web browser and navigate to `http://localhost:8080` to access the game.

You will then see the load user page, where you can enter a username and age. Repeat this again for the next player. Then hit submit.
The next page will be the game board where you can start to play, simply click the square that you want to make your move in.

## Technologies Used

- Python: Server-side logic implemented with Python using the Bottle web framework.
- HTML/CSS/JavaScript: Front-end interface built using standard web technologies for a visually appealing and interactive experience.
- Bottle Framework: Utilized for handling routing and server-side logic, facilitating communication between the client and server.
- SQLite3: Used for persistent storage.

## Contributors

- Flavio Cesar Mendoza Trinidad
- Said Khan
- Kaleb Rowe
- Christopher
- Mohammad Fahmidul Islam

## Note for the marker

### We added the marking scheme and the correlation between each component, this can be refered to at your convenience. ###

- The UML diagrams are in the Uml_diagrams folder
- The documentation for each moduule is in the arch_documents folder
- All the meeting notes are in the meeting_notes folder
- Code reviews are in the code review folder. Note that for sprint 1 code review we didn't have a formal process in place but we sent an email to the prof to help him trace our verbal reviews.
- Each peer assesment has been grouped in the peer assesment folder
- Each user story is in the user story folder under docs.
- the GameFramework is also under the docGameFramework folder under docs. There is a framework file and userManual file

## Sprint 2 group marking Scheme

- Properly minuted SCRUM meetings and decisions (20%) **[All meetings follow the template we made to ensure each requirement is met ]**
  - This will be weighted by the number of properly conducted meetings held on regular basis and quickly available in the repo. **[For sprint two we held and documented a meeting every Monday, Wednesday, and Friday]**
  - **5 points** agenda coverage for each meeting includes progress review with kanban and issue tracker **[Each note has a progress review that links the related kanban and/or issue]**
  - **4 points** decisions documented properly with response plan and reflected in the Kanban Board/issue tracker **[Each meeting has an agenda section where agenda items are listed]**
  - **3 points** changes to architecture and low level designs (interfaces) discussed, determined, and documented. Architecture documents adjusted accordingly. **[All changes to architecture are discussed and documented in the meeting notes and codereview files under the docs folder]**
  - **2 points** SCRUM master and notetaker roles rotated among team **[Each member of the team has been SCRUM master and notetaker at least once]**
  - **3 points** Meetings committed and pushed regularly, so team members can access. **[Each meeting note is pushed to the master in a new file as they're taken so teammembers can view and refer to them]**
  - **3 points** Reasonable distribution of tasks among team. Design interface/services and Coding tasks assigned to individual team members. Tasks on KanBan board. **[Tasked have been assigned and documented in the kanban, while being distrubuted evenly based on the workload]**

- Maintenance of the Kanban Board and the issue tracker in your project repository (15%)
  - Kanban board must be set up early in the first sprint. **[Our Kanban board was well set up in the first sprint]**
  - **2 points** Consistent continuous use. Assignment, labels, color coding, categories, etc. used appropriately and consistently by team. **[Kanban has been consistently used and updated throughout sprint one and two]**
  - **5 points** Create cards for backlog features, required functionality for sprint 2, and assigned tasks. **[Cards are set up for backlog fetures, as well as required functionality, each task is assignened to a member]**
  - **3 points** Progress of tasks/issues noted on board and tracker **[Tasks move from backlog, to in Progress, to Done]**
  - **5 points** New issues (tasks) arising in meetings, reviews and otherwise are noted on issue tracker (board) **[each issue in a meeting note is assigned and linked to a issue tracker]**

- New performance reviews for sprint II (how did the team members perform) conducted and documented (5%)
  - **5 points** Each team member assessed, by each other team member. Serious performance reviews including problems/personality clashes and possible solutions. A trivial review indicating everyone did fine will be assumed to be pro-forma and will be given no credibility. Problems with the team progress, dynamics and process must be identified and documented, and tracked with possible responses and progress on those items becoming kanban/agenda items. If you have no issues with a particular team member, you can at least make a suggestion for their project activity.

    **[New performance reviews for sprint II have been added. Each team member has reflected on the sprint one feedback, and although there wasn't much time in sprint two we attempted to give everyone something cretical they could improve on.]**

- Code reviews conducted and documented. (20%) **[We have now started documenting our code reviews for sprint two. The Code review takes the same process we did for sprint one, but is now documented in the Code_review folder in the docs folder]**
  - Code should be regularly presented and discussed as a team, not just at end of cycle. **[code is review before each merge by entire team. Code reviews were done every class day of the sprint 2]**
  - **5 points** Code review details incorporated into process model and pull requests. **[Code review is noted in our SoftwareProcessModel documentation There is a section saying changes since sprint 1]**
  - **10 points** Code reviews are thorough, including style issues. **[Code reviews are thorough and include a section for style/conventions for example code review April 1st is super detailed]**
  - **3 points** All code should be reviewed by entire team before pull request is merged. **[All members attened code reviews, attentence recorded in the documentation]**
  - **2 points** Pull request deadlines for code contributions established and enforced. **[Deadlines noted in the code reivew documentation]**
  
- User stories (10%) **[User stories were added to the userStories folder in the docs folder]**
  - **5 points** Stories offer comprehensive description of a imagined interaction with the system (either as working as imagined) with sufficient detail to implicate design suggesitons. **[Each user story is detailed and unique]**
  - **5 points** One story and one feature suggestion per member. Story should suggest a new feature that is not obvious, so that user stoiry has contributed to the backlog of ideas. **[Each member provided a user story, the ideas where added to the backlog]**

- Component Architecture Documents (5 %)
  - These should be updated as your project design matures during the sprint
    - **5 points** Details of components and interfaces documented correctly **[Architecture documents have been updated to reflect the curret product]**

- docGameFrame Framework proposal document (15%) **[this is saved to a folder in the docs folder called docGameFramework]**
  - **5 points** Document(s) shows refactoring of module as needed with interface changes and arch diagrams as needed to illustate changes. **[Documents for each component are all saved in this folder.]**
  - **5 points** Redesign comparison to existing arch is illustrated with overall and module diagrams that use consist format. **[Redesign is located in the GameFramework.md]**
  - **5 points** How to use framework is clear from description and shows understanding of decoupling issues involved with each project module. **[Instructions are in the FrameworkUserGuide.md]**

- Process Model Document (5 %)
  - **5 points** Elements of process identified and explained. Distinction made between process and process model. **[Process model is documented in the docs folder under a file called SoftwareProcessModel.md Update from sprint 1 has been indicated]**

- Sprint (end) release status (5%)
  - **5 points** operation of software and available features clear from documents and video/user manual [ UserGuide.mp4 video upated for final project]

- Code reviews conducted and documented from sprint 1. (20 %) **[Sprint 1 code review wasn't documented, we made sure to document our code review so it meets the following requirements. An email was sent to the prof regarding sprint 1's code review]**
  - Code should be regularly presented and discussed at SCRUM meetings, not just at end of cycle.
  - **5 points** Code review details incorporated into process model and pull requests.
  - **3 points** Code contributions are presented to entire team.
  - **10 points** Code reviews are thorough, covering style issues (SOLID, de-coupling) as well as correctness.
  - **5 points** All code should be reviewed by entire team before pull request is merged.
  - **2 points** Pull request deadlines for code contributions established and enforced.
