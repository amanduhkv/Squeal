# Squeal
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-wiki">Project Wiki</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#sample-features">Sample Features</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#the-team">The Team</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
![squeal-logo]

[squeal-logo]: ./assets/squeal-in-logo.png

[Squeal](https://squeal-yelp.herokuapp.com/) is a web application inspired by Yelp and created by a team of 4 software engineers.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Project Wiki
* [Backend API Documentation](https://github.com/amanduhkv/Squeal/wiki/Backend-API-Documentation)
* [Database Schema](https://github.com/amanduhkv/Squeal/wiki/Database-Schema)
* [Features List](https://github.com/amanduhkv/Squeal/wiki/Features-List)
* [Redux State Shape](https://github.com/amanduhkv/Squeal/wiki/Redux-Store-Shape)
* [Frontend Routes](https://github.com/amanduhkv/Squeal/wiki/User-facing-(Frontend)-Routes)
* [User Stories](https://github.com/amanduhkv/Squeal/wiki/User-Stories)


### Built With
#### Frameworks, Platforms, & Libraries:
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)

#### Database:
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

#### Database:
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SAMPLE FEATURES -->
## Sample Features
### Search:
![Search](https://i.imgur.com/e75RInS.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

1. Clone the repo:

    SSH version:
    ```sh
    git clone git@github.com:amanduhkv/Squeal.git
    ```
    or

    HTTPS version:
    ```sh
    git clone https://github.com/amanduhkv/Squeal.git
    ```

2. Install packages
    ```sh
    pipenv install
    cd react-app
    npm install
    ```
3. Create a .env file and set the environment variables for SECRET_KEY and DATABASE_URL to your choosing.

4. Migrate and seed the files.
    ```sh
    flask run db init
    flask run migrate
    flask seed all
    ```
5. Run the server and start the react app
    ```sh
    pipenv run flask run
    cd react-app
    npm start
    ```

<!-- ROADMAP -->
## Roadmap

- [x] Businesses
    - [x] Create a business
    - [x] Load all businesses
    - [x] Load a business by detail
    - [x] See list of current user's businesses
    - [x] Update a current user's business
    - [x] Delete a current user's business
- [x] Search / Filter
    - [x] Create a search filter
    - [x] See the result of a search filter
    - [x] Update a search filter
    - [x] Remove a search filter
- [x] Reviews
    - [x] Create a review
    - [x] Load all user's reviews
    - [x] Load all of a business's reviews
    - [x] Update a current user's review
    - [x] Delete a current user's review
- [x] Images
    - [x] Create a business image
    - [x] Create a review image
    - [x] Delete a business image
    - [x] Delete a review image


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## The Team

Amanda Vien:
<br>
[![linked in][linkedin-icon]][linkedin-url-amanda]
[![linked in][github-icon]][github-url-amanda]
<br>

Brandon Tasaki:
<br>
[![linked in][linkedin-icon]][linkedin-url-brandon]
[![linked in][github-icon]][github-url-brandon]
<br>

Jae Hwang:
<br>
[![linked in][linkedin-icon]][linkedin-url-jae]
[![linked in][github-icon]][github-url-jae]
<br>

Michael Jung:
<br>
[![linked in][linkedin-icon]][linkedin-url-michael]
[![linked in][github-icon]][github-url-michael]
<br>


Project Link: [https://github.com/amanduhkv/Squeal](https://github.com/amanduhkv/Squeal)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-icon]: https://skillicons.dev/icons?i=linkedin
[github-icon]: https://skillicons.dev/icons?i=github
[linkedin-url-amanda]: https://www.linkedin.com/in/amandakvien/
[linkedin-url-brandon]: https://www.linkedin.com/in/brandon-tasaki/
[linkedin-url-jae]: https://www.linkedin.com/in/jae-hwang-71654490/
[linkedin-url-michael]: https://linkedin.com/in/michael-h-jung/
[github-url-amanda]: https://github.com/amanduhkv
[github-url-brandon]: https://github.com/MacFlyOSX
[github-url-jae]: https://github.com/jaeyoungh1
[github-url-michael]: https://github.com/michaelhjung
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
