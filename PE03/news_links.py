import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the Hacker News website*
url = "https://news.ycombinator.com/news"
response = requests.get(url)

# Step 2: Check if the request was successful*
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find all <a> tags and filter only story links*
    story_links = soup.select('.titleline a')

    # Step 4: Save the titles and links* 
    with open("hacker_links.txt", "w", encoding="utf-8") as file:
        file.write("Links from Hacker News:\n\n")
        for link in story_links:
            title = link.get_text()
            href = link.get('href')
            if href:
                print(title)
                print(href + "\n")
                file.write(title + "\n")
                file.write(href + "\n\n")
else:
    print("Failed to fetch page. Status code:", response.status_code)
