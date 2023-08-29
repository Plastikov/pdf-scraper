import os
import re
import requests
import subprocess
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument("-url", "--target_url", help="The url you would like to crawl")
parser.add_argument("-info", "--search_info", help="The information you would like to search in the pdf")

args = parser.parse_args()

try:
    response = requests.get(args.target_url)
except Exception as e:
    print(f"Error: {e}")
soup = BeautifulSoup(response.text, "html.parser")

divs = soup.find_all("a")
links = []

for div in divs:
    href = div.get("href")

    if href.find(".pdf") > -1:
        links.append(href)

num_pdf = len(links)
print(f"There are {num_pdf} pdfs to work with")

iterations = 0

while len(links) > 0:
    for i in range(10):
        link = links.pop(0)
        response = requests.get(link)

        filename = f"test-gazette-file{i+1}.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        
        text = subprocess.run(["pdftotext", filename, "-"],
                              capture_output=True).stdout.decode("utf-8")

        info = re.search(args.search_info, text)
        if info:
            print(info.group(0))
        else:
            print(f"No match found. {filename} has been searched.")

    os.system("rm test-gazette-file*.pdf")

    iterations += 1

    print(f"Loop iteration {iterations} complete. Continuing...")