# TOOLS-IN-DATA-SCIENCE
This repo contains project done by me in the course of tools in data science which is part of BSC degree in Programming and Data Science from IIT Madras.
**Course Instructor:- Anand S (Co-founder & CEO, Gramener)**
**Project-1: Basel:10**

![Tools In Data Science](https://github.com/user-attachments/assets/b20faecc-b2fe-4a52-b505-79727e882503)

# GitHub Basel Users Data
- This project uses the GitHub API to retrieve profiles of users in Basel with over 10 followers and their public repositories.
- The analysis of the repository data reveals that while developers in Basel are actively creating projects, many of these repositories struggle with low visibility and engagement, as evidenced by the minimal stargazer counts. Additionally, features like wikis and project boards are often underutilized, indicating missed opportunities for better documentation and community interaction. 
- To gain traction or to enhance project success, developers should focus on improving documentation, actively promoting their work on social media, and leveraging available features to foster collaboration. By aligning their efforts with popular programming languages and frameworks, they can increase their chances of attracting more users and contributors..

## Project Overview
This repository contains data on GitHub users located in Basel, Switzerland, with more than 10 followers. The data includes user profiles and details of their public repositories.

### Files Included
1. `users.csv`: Contains details of each user such as their username, company, location, email, bio, number of followers, etc.
2. `repositories.csv`: Contains repository information for each user, with fields such as repository name, creation date, stars, watchers, programming language, and license type.
3. `TDS_Project_1.ipynb`:Contains code used for the retrival of the data.
#### Code Details
The `TDS_Project_1.ipynb` script uses the GitHub API to:
- Find users in Basel with more than 10 followers.
- Fetch detailed information about each user.
- Retrieve up to 500 of each user’s public repositories.
The results are saved in `users.csv` and `repositories.csv`.

##### Usage
1. Ensure you have a GitHub personal access token and add it to the script where indicated.
2. Run the script using:
   ```bash
   python TDS_Project_1.ipynb

