import requests
import os
import bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # Create a directory to store all the downloads

while not url.endswith("#"):
    print("Downloading the page...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    comic_element = soup.select('#comic img')

    if not comic_element:
        print("No comic image found!!")
    else:
        comic_image_url = comic_element[0].get('src')
        print("Downloading the image %s..." % (comic_image_url))

        res = requests.get('http:' + comic_image_url)
        res.raise_for_status()

        with open(os.path.join('xkcd', os.path.basename(comic_image_url)), 'wb') as file:
            file.write(res.content)

    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print("Done")
