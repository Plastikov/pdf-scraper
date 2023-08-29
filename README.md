---
# pdf-scraper
A tiny system to help you find information in bulk pdfs

This Python script is designed to crawl a target website for PDF links, download the PDF files, extract text from them, and search for specific information within the extracted text.

## Usage

To use the script, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the required libraries by running the following command:

```
$ pip install requests beautifulsoup4

```
3. Additionally, you need to have the `pdftotext` utility installed on your system. This utility is used to convert PDF files to text. You can install it on Ubuntu/Debian using:

```
$ sudo apt-get install poppler-utils
```
4. Save the script to a file, for example, `pdf_crawler.py`.
5. Open your terminal and navigate to the directory containing the script.
6. Run the script using the following command:

```
$ python pdf_crawler.py -url <target_url> -info <search_info>
```

Replace `<target_url>` with the URL of the website you want to crawl for PDF links.
Replace `<search_info>` with the text you need to find within the pdfs.

## Script Overview

This script performs the following tasks:

1. It takes a target URL as a command-line argument, `-url`, which specifies the website to crawl.
2. The script uses the `requests` library to make an HTTP request to the target URL and fetch the HTML content.
3. It utilizes `BeautifulSoup` to parse the HTML content and find all `<a>` elements (links) within the page.
4. The script filters out links that have ".pdf" in their `href` attribute, indicating PDF files.
5. It downloads the PDF files and saves them to the current directory with filenames like `test-gazette-file1.pdf`, `test-gazette-file2.pdf`, and so on.
6. For each downloaded PDF, it uses the `pdftotext` utility to convert the PDF content to text.
7. The script searches for specific information in the extracted text. In this example, it searches for the text "holidays declared, official weekends."
8. If the specified information is found, it prints the matched text; otherwise, it prints an error message indicating no match was found.
9. After processing a batch of 10 PDFs, it removes the downloaded PDF files.
10. The script continues this process in a loop until all links have been processed.

Please note that this script is designed for educational purposes and might require adjustments to fit specific use cases. Make sure to adhere to website terms of use and copyright regulations when crawling and downloading content.
---
