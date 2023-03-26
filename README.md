# Amazon Scraper

Get product name and price from all "Acer Chromebook Enterprise Spin 714" search results on Amazon.

### Purpose 

Collect marketing price of Chromebooks from Amazon listings. If a cron job is scheduled in the local machine to run this scraper on a daily or weekly basis, we are able to analyze the marketing trend, and use this data to allocate resources and prioritize projects.


### Development Focus

- Use `Python` and a library called `Beautiful Soup` to locate the html elements that contain the target information: Product name and Price.
- Capture the total search results from the `span tag` and store it in the total_results variable and increment the variable every time a listing is scraped.
- Implement a `while loop` to increment the page number to go to the next page of search results. Break out the loop when the scraped_results has reached the total_results. 
- Set up  `Rails` server with `CRUD` actions and routes in controller and routes.rb.
- Store scraped data in `PostgreSQL` database by submiting `POST` requests to the server when the program runs.
- Export data from chrome_books table to a `CSV` file for `data analysis` or other usage.


### Potential Implementations

- Upload the csv file to Tableau or other BI tools to analyze the marketing insights.
- Set up cron jobs or other scheduling tools to run this program automatically on a regular basis.
- Send out emails or other types of notifications when an unusual situation happens.

### Sample Data Scraped in JSON format

![Screenshot 2023-03-25 230808](https://user-images.githubusercontent.com/115205162/227753136-eac7fbbf-b693-41b9-892b-edaa955ad076.png)
To see all scraped data, check out chrome_books.csv. For this specific product, there were 40 search results in total when this program ran.

### Setup Instructions

1. Make sure Python, Ruby, and Rails are installed.

2. Clone the repository and cd into the folder.

3. Run the below command in the terminal to install all depandencies.
```
pip freeze > requirements.txt
```
4. cd into the server folder and run Rails server by running the below command.
```
rails server
```
5. Go to this website to find out your User Agent: https://www.whatismybrowser.com/detect/what-is-my-user-agent/ and replace my user agent in app.py headers with your user agent.

6. Run the below command to run the program and put the data in the PostgreSQL.
```
python app.py
```
7. To view the data, you can make a GET request to the server end point `http://localhost:3000/chrome_books` in the browser, via Postman, or open psql in the terminal and query the data with SQL.
Open psql by running this command:
```
psql -U <userName>
```
Inside psql, run this SQL query to see all data in the chrome_books table:
```
SELECT * FROM chrome_books;
```

8. To copy the data into a new csv file, run this SQL query in psql:
```
COPY chrome_books TO '/tmp/<fileName>.csv' WITH CSV HEADER;

```
and you will find the csv file in your tmp directory!


### Finally...
Happy scraping and analyzing! 📈
