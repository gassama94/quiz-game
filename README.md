# Quiz Game
Welcome to my Quiz Game! This is a simple Python program that asks questions about the capital cities of different European countries and checks if the provided answers are correct.

# Table of Contents

- [Introduction](#introduction)
- [User Experience](#user-experience)
- [Features](#features)
- [Technologies used](#Technologies-used)
- [Programes used](#programes-used)
- [Questions](#questions)
- [Testing](#tesing)
- [Bugs and Issues](#bugs-and-issues)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Getting Started](#getting-started)
- [Game Rules](#game-rules)


## Introduction
This is project number three out of five for Code Institute full-stack development program: Python Terminal.
[Live Project](https://quiz-gamee.herokuapp.com/)

The Quiz is made in the Python terminal and runs in the Code Institute mock terminal Heroku. The Quiz will test the player's knowledge about some of the worlds mysteries!

## How to Play

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the game:
5. Answer the questions by typing the name of the capital city in lowercase.
6. The program will tell you if your answer is correct or incorrect.
7. Enjoy playing the Quiz Game and test your knowledge of European capital cities!

## User Experience - UX
### User Stories
- With this app my goal is to:
1. Build a clean and easy app to use.
2. Build a game that is challenging for the player.
3. As a new user i want to:
4. Being welcomed and understand what the game is.
5. Get knowledge of hom many points each question is worth.
6. Know how well i did in the quiz with score and time tracking functions.

## Features
### Intro Message
Welcomes user and informs them about the topic of the quiz. After that user gets the question if they wish to start the game, if yes a timer is displayed to prepare the player.

### Game features
- The quiz contains of 5 questions with 5 alteratives each.
- The game displays correct or incorrect straight after answer.
- The game keeps track of users total score.

## Technologies Used
### Languages Used
- Python

## Programmes Used
- GitPod: Used to create and edit the app.
- GitHub: Used to store the code after being pushed from GitPod.
- Heroku: Used to deploy the live project!
- PEP8: was used to validate all the python code.


## Questions

The Quiz Game includes the following questions:

- What is the capital city of France?
- What is the capital city of England?
- What is the capital city of Norway?
- What is the capital city of Italy?
- What is the capital city of Sweden? etc


# Testing
[Extebdclass](https://extendsclass.com/python-tester.html)
The extendclass validator makes sure there are no syntax errors in the python file and has been used throughout the project.

## Bugs And Issues
- Invalid inputs would freeze the game Solution: Gave an error message.
- The app would continue forever after quiz was finished Solution: Gave the user a choice to restart the game or shut down.
- The code was unneccesarily long and hard to read Solution.

## Deploying This Project
- Log in to Heroku or create an account
- On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
- You must enter a unique app name
- Next select your region
- Click on the Create App button
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
- Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
- Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
-  Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
- Scroll to the top of the page and choose the Deploy tab
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and customize the Quiz Game according to your needs. Happy playing!

