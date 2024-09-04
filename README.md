# THE NET (Social Media Website)
## Tech Stack:

- Languages & Frameworks: Python (Django), HTML/CSS/JavaScript
- Database: SQL (SQLite3)
- Containerization: Docker

## Overview
THE NET is a full-stack social media platform designed to allow users to engage with content through posts, likes, comments, and following other users. After registering and logging in, users can freely share their thoughts, interact with others, and build a community.

## Features
### User Authentication & Authorization:
Secure registration and login system, with all user data stored in an SQLite3 database.

### Interactive User Experience:
Real-time updates for likes, comments, and post edits, implemented using JavaScript and asynchronous JSON communication between the front-end and Django-powered back-end.

### Scalable & Consistent Deployment:
The application is containerized with Docker, ensuring a consistent environment across development and production.

### Site Administration Page:
- There is an administration page (https://0.0.0.0:8000/admin) that allows site managers to easily manage the database such as adding, deleting, and modifying the posts as well as likes and comments. 
- One existing administration account is: username: admin, password: admin

## Getting Started
- Clone the repository.
- Set up the environment using Docker.
- Run $docker-compose up
- Go to 0.0.0.0:8000 on your browser

# Credits
- layout.html: Portions of code were adapted from [CS50’s Web Programming with Python and JavaScript](https://cdn.cs50.net/web/2020/spring/projects/4/network.zip)

This project is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. This is a human-readable summary of (and not a substitute for) the license. Official translations of this license are available in other languages.

You are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- NonCommercial — You may not use the material for commercial purposes.
- ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
