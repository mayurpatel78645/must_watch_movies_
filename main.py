import requests
from bs4 import BeautifulSoup

request = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response = request.text
soup = BeautifulSoup(response, "html.parser")

titles = [title.getText() for title in soup.select(".title") if ")" in title.getText()][::-2]

with open("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")
