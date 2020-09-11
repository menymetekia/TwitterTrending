# TwitterTrending

This project consists of two seperate components:

Ingestion component: Ingests twitter tweets and stores them in a MongoDB database.
Trends API component: REST API used after ingestion to provide the twitter trends within a certain time range.

## Running using Docker:

This project uses docker-compose to create containers for the MongoDB database, ingestion component and trends api component.

MongoDB:

**docker-compose up --build -d mongodb**

Ingestion:

**docker-compose up --build ingestion**
<br>
The component will start ingesting tweets made in or around Amsterdam within the last 72 hours in batches of ~100. This process can be canceled prematurely if enough tweets have been retrieved. 
<br>
<br>
Trends api:
<br>
**docker-compose up --build trends_api**
<br>
After the component starts running it is possible to send a GET request to:
<br>
http://127.0.0.1:5000/trends/<last-x-hours>
<br>
<br>
Example:
<br>
Get trends for the last 3 hours
<br>
http://127.0.0.1:5000/trends/3
  
