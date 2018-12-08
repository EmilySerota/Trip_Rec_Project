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

![MYRECS homepage logged out](/static/screenshots/homepage-logged-out)
<br/><br/><br/>
Register or login to create new or edit your recommendations. If a user chooses not to login they can still search for existing recommendations, but cannot create or edit recommendations. 






## For Version 2.0

- **Further map functionality:** Markers added at different locations to help with itinerary planning
- **Ratings:** Pull in rating for different activities or establishments
