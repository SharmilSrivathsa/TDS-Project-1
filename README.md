![App Screenshot](https://miro.medium.com/max/693/1*X465HGyHWV-pMzvxqM9xDQ.jpeg)
# TOOLS-IN-DATA-SCIENCE

This repo contains project done by me in the course of tools in data science which is part of BSC degree in Programming and Data Science from IIT Madras.
<br />Course Instructor:- Anand S (Co-founder & CEO, Gramener)

# GitHub Basel Users Data

- This project uses the GitHub API to retrieve profiles of users in Basel with over 10 followers and their public repositories.
- Analysis reveals that most users have repositories with under 5 stars, showing room for improvement in community engagement.
- To gain traction, developers should focus on improving repository descriptions and actively contributing to open-source projects.

## Project Overview

This repository contains data on GitHub users located in Basel, Switzerland, with more than 10 followers. The data includes user profiles and details of their public repositories.

### Files Included

1. `users.csv`: Contains details of each user such as their username, company, location, email, bio, number of followers, etc.
2. `repositories.csv`: Contains repository information for each user, with fields such as repository name, creation date, stars, watchers, programming language, and license type.

### Code Details

The `Code.py` script uses the GitHub API to:
- Find users in Basel with more than 10 followers.
- Fetch detailed information about each user.
- Retrieve up to 500 of each user’s public repositories.

The results are saved in `users.csv` and `repositories.csv`.

### Usage

1. Ensure you have a GitHub personal access token and add it to the script where indicated.
2. Run the script using:
   ```bash
   python code.py

