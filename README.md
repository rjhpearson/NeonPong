# NEON PONG
#### Video Demo:  https://www.youtube.com/watch?v=5mWoAtb3j4M
#### Description:
## About

This project is my final project for Harvard University's CS50x Introduction to Computer Science Course.

I've always wanted to build my own game, and given this is my first project, it felt right to try and recreate the arcade classic Pong.

Neon Pong has many similar features to Pong, but with a few upgrades I'll explain throughout this document.

**You can view my submitted video <a href="https://www.youtube.com/watch?v=5mWoAtb3j4M&t=4s">here</a>.**

# How to play
## Controls
#### Player 1
- Press either 'W' or 'S' to move the paddle 'UP' or 'DOWN' respectively.
#### Player 2
- Press either 'UP ARROW' or 'DOWN ARROW' to move the paddle 'UP' or 'DOWN' respectively.

## Game Mechanics
- Each Player must provide a name in their respective Player input field.
- Select 'Start Game' to begin.
- The objective is for players to return the ball back to their opponent using their paddle.
- If you fail to return the ball, your opponent scores a point.
- Scores are displayed at the top of the screen.
- The first player to reach a score of 3 wins the match.
- At the end of the game, you can either rematch, or return to the title screen.
- The winner's details, such as their name and score are recorded in a database (along with the date/time of the win)
- Winner details are presented on the main screen.

## Features & Implementation

Neon Pong and made using HTML, CSS and A LOT of Scalable Vector Graphics (SVGs). These are manipulated by JavaScript within the DOM. I have a separate JS file to control the behaviour of the stars.

Underpinning all of this is a Python project, using the Flask framework. There is also some additional AJAX that sends the winner details in JSON format back to Flask so they can be written to the database using Python.

### Features of Note:
- The Game features the same sound effects used in the original Pong
- The 'Neon' art style comes from my love of the 80's and <a href="https://www.youtube.com/watch?v=4xDzrJKXOOY">Synthwave</a>.
- The 'Star' effects were inspired by Kingdom Hearts (when you strike an enemy/heartless)
- The 'Music' (which can be toggled on/off) is from <a href="https://en.wikipedia.org/wiki/Dizzy_%E2%80%93_The_Ultimate_Cartoon_Adventure">Dizzy – The Ultimate Cartoon Adventure</a>. (Gameplay can be found <a href="https://www.youtube.com/watch?v=LRYdU0NXYMc">here</a>)
- Winner's details are stored in a SQL database
- In order to pass the JavaScript variables back to Flask, I used AJAX

## How the project evolved
I came into this course knowing my end goal was to create my first game. I'd dabbled in Unity, and was aware of both LÖVE 2D and Godot, but CS50 hadn't quite covered these subjects, so it didn't feel right to use them. Following the lecture on JavaScript and how it could manipulate objects within a page, I thought about how I might be able to manipulate Scalable Vector Graphics (SVGs). I'd used them at work but only as static images. With JavaScript however, I was now able to change these using interactions (such as buttons and key presses). I ran a few tests and was amazed to find I could manipulate SVGs around the page. The implications of this were mind blowing, and I set about the task of trying to recreate the original 'Pong'.

I was successful in creating a single black backgrounded SVG, with 2x white rectangle SVG's as paddles, a white square for a ball, and using JS's animation functions (window.requestAnimationFrame(step);) I was able to create an animation loop which acted as my game loop. I was now able to animate and move SVG on the screen.

I implemented logic around when an SVG's coordinates touch, signalling when the ball should change directory or trigger the end of a round. I added scoring variables, had the speed of the ball’s velocity increase with each bounce, and started to play with sounds and music. The screen was quite bare, so I added a 'court', drawing inspiration from 1980's air hockey games. I added the signature 'neon' glow using box shadows and added SVGs to display the player's scores. However, I felt I could go further.

I had a great time implementing the stars that generate when the ball hits a paddle. I added different sizes and trajectories, randomising them to give them character. I placed the script in a separate file as I was struggling to implement these without affecting the rest of the code. I'm really happy with how they turned out.

I created a title page with instructions on how to play the game, and a button to start it. The game was feeling relatively complete, however having reviewed some to the projects other students had done, I realised that my game was rather 'ephemeral'. It launched, you started the game, played it and then once finished, it just ended/froze. There was no record of who'd played the game or re-playability without refreshing the page. Lots of other projects were using SQL to store data or pass information back to a web server. It was at this point I decided to change things up.

I turned my project into a Flask Project. I thought that if I could utilise Flask, like in CS50 Finance, I could write data back to a Database (such as scores) and present it on my title screen. There was one major hurdle. How to get my JS variables back to Flask? Enter AJAX!

AJAX allowed me to pass a JSON Object back to Flask where I could Parse it and write the data into SQL. Getting this to work was a game changer (no pun intended) and I now had a way of capturing scores in SQL. I added 2 text input fields for players to add their names, some logic which hid the start button until both names were added, and now I was able to capture and save the player's details.

I added a lot more logic around what happens when the match is over. I provided the options of a rematch or returning to the title screen to start afresh with new players. I locked down the player inputs once the game had started so they couldn't be changed mid game (I could have saved these as variables, but time was getting on).

After a LOT of bug fixes (auto-playing music on start of a screen is NOT a good idea), tidying up, changing my mind about almost everything (such as how big the game screen should be, what data should I capture), I finally finished on a product I'm happy with.

I hope you enjoy playing it as much as I enjoyed making it :)

## Project Structure

- app.py is the Flask project
- index.html is the main body of the project. It contains lots of SVGs that are manipulated around the page.
- stars.js is a script to manage the animation of stars when the ball hits a paddle
- scores.db stores the scores
- AJAX is used to get scores into a JSON and back to Flask ('/process' 'POST' method in app.py)

## Misc

This project was developed by me as a final project for Harvard University's <a href="https://cs50.harvard.edu/x/2023/">CS50x Introduction to Computer Science Course</a>.

Thank you to Harvard University, Prof. David J. Malan, Prof. Brian Yu, Prof. Doug Lloyd and the CS50 staff!

Also, a BIG shout out to the staff on CS50 Discord (curiouskiwi and Blauelf especially!)

## Contact

Please feel free to contact me <a href="mailto:rjhpearson@yahoo.co.uk">here</a> if you have any questions.
