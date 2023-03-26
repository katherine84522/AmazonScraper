import requests
from bs4 import BeautifulSoup
import time


page = 1

# initialize variables for total number of results and number of results scraped
results_scraped = 0

url = f"https://www.amazon.com/s?k=Acer+Chromebook+Enterprise+Spin+714&page=4&crid=1UE647NGJBQAH&qid=1679758022&sprefix=acer+chromebook+enterprise+spin+714&ref=sr_pg_1"
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

response = requests.get(url, headers=HEADERS)
print(response)
soup = BeautifulSoup(response.text, "html.parser")

total_results_elem = soup.find(
    "div", {"class": "a-section a-spacing-small a-spacing-top-small"})
total_results_span = total_results_elem.find_all("span")[0]
total_results_text = total_results_span.text.strip()
total_results = int(total_results_text.split()[2].replace(",", ""))
print(f"Total search results: {total_results}")


while True:
    url1 = f"https://www.amazon.com/s?k=Acer+Chromebook+Enterprise+Spin+714&page={page}&crid=1UE647NGJBQAH&qid=1679758022&sprefix=acer+chromebook+enterprise+spin+714&ref=sr_pg_{page}"
    response = requests.get(url1, headers=HEADERS)
    print(f"Scraping page {page}...")

    if response.status_code == 200:
        soup1 = BeautifulSoup(response.text, "html.parser")

        results = soup1.find_all(
            "div", {"data-component-type": "s-search-result"})

        final_results = results[2:]

        # loop through each search result on the page
        for result in final_results:
            name = result.find(
                "span", {"class": "a-size-medium a-color-base a-text-normal"}).text.strip()
            price = result.find("span", {"class": "a-price-whole"})
            if price:
                price = price.text.strip()
            else:
                price = "N/A"

            url1 = "http://127.0.0.1:3000/chrome_books"
            headers = {"Content-Type": "application/json; charset=utf-8"}
            data = {
                "name": name,
                "price": price
            }
            response1 = requests.post(url1, headers=headers, json=data)
            print("Status Code", response1.status_code)
            # print("JSON Response ", response1.json())
            # print(f"Product name: {name}")
            # print(f"Price: {price}")

            # increment the counter for the number of results scraped
            results_scraped += 1
            print(results_scraped)
            # check if we have scraped all the search results
            # if results_scraped >= total_results:
            #     print("Finished scraping all search results.")
            #     break

        # break the loop if we have scraped all the search results
        if results_scraped >= total_results:
            break

    else:
        print(
            f"Failed to scrape page {page} with status code {response.status_code}.")

    # add a delay between requests to avoid getting blocked
    time.sleep(2)

    # increment page counter
    page += 1
