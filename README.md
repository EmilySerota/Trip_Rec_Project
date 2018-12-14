# MYRecs

## Summary

**MYRecs** is a user login based application that allows users to easily create, update, and search for recommendations when traveling to different cities around the world. MYRecs eliminates the time spent scanning travel sites, blog posts, and following up with friends for recommendations, as you can easily create or search for recommendations by username or city. 

## About the Developer

MYRecs was created by Emily Serota. Learn more about the developer on [LinkedIN](https://www.linkedin.com/in/emily-serota).

## Technologies

**Tech Stack:**

- Python
- Flask
- SQLAlchemy
- Jinja2
- HTML
- CSS
- Javascript
- Bootstrap
- Google Geocode API

MYRecs is an app built on a Flask server with a PostgreSQL database, and SQLAlchemy as the ORM. The front end consists of Jinja2, HTML, Bootstrap, and Javascript. The user login in utilizes password salting and the hashlib. The map is built using the Google Geocoding API.

![screen shot 2018-12-14 at 1 54 32 pm](https://user-images.githubusercontent.com/38198868/50034698-f71dff80-ffb2-11e8-9cee-e564eedf41ab.png)
![screen shot 2018-12-10 at 9 52 39 pm](https://user-images.githubusercontent.com/38198868/49908135-0162c100-fe2e-11e8-8e83-f6ab81bf82e2.png)
<br/><br/><br/>
Register or login to create new or edit your recommendations. If a user chooses not to login they can still search for existing recommendations, but cannot create or edit recommendations. 

![screen shot 2018-12-14 at 1 49 33 pm](https://user-images.githubusercontent.com/38198868/50034545-3435c200-ffb2-11e8-9f21-4cd97c893c85.png)
<br/><br/><br/>
Login to see create/edit capabilities

![screen shot 2018-12-14 at 1 49 47 pm](https://user-images.githubusercontent.com/38198868/50034800-685db280-ffb3-11e8-8a9e-d5861306c692.png)
Once a user is logged in they have more capabilities

![screen shot 2018-12-14 at 1 50 10 pm](https://user-images.githubusercontent.com/38198868/50034573-61827000-ffb2-11e8-8d76-a20d51a1b6a1.png)
<br/><br/><br/>
Create a new recommendation

![screen shot 2018-12-14 at 1 52 23 pm](https://user-images.githubusercontent.com/38198868/50034595-84148900-ffb2-11e8-9303-b6b0a2e298c8.png)
![screen shot 2018-12-14 at 1 53 07 pm](https://user-images.githubusercontent.com/38198868/50034648-c9d15180-ffb2-11e8-8ed6-ed1c0d6aff19.png)
![screen shot 2018-12-14 at 1 52 41 pm](https://user-images.githubusercontent.com/38198868/50034599-8d055a80-ffb2-11e8-9501-9488d50a095e.png)
<br/><br/><br/>
View the recommendation

![screen shot 2018-12-14 at 1 53 27 pm](https://user-images.githubusercontent.com/38198868/50034726-1321a100-ffb3-11e8-9adf-9527828cd850.png)
Edit the recommendation

![screen shot 2018-12-14 at 1 54 16 pm](https://user-images.githubusercontent.com/38198868/50034750-2b91bb80-ffb3-11e8-9e59-05a0f28e7e68.png)
![screen shot 2018-12-14 at 1 53 48 pm](https://user-images.githubusercontent.com/38198868/50034761-35b3ba00-ffb3-11e8-887d-bcdcb67baca4.png)
View recommendations by location or username







## For Version 2.0

- **Further map functionality:** Markers added at different locations to help with itinerary planning
- **Ratings:** Pull in rating for different activities or establishments
