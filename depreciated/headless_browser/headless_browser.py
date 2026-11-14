# Using a Headless Browser
# Written by Joe Manlove
# last revision 11/9/2020
# loosely based on https://realpython.com/python-web-scraping-practical-introduction/#install-mechanicalsoup

# mechanical soup provides a headless browser so we can parse JS heavy sites.
import mechanicalsoup

# this is the URL for Kern Community College District HR with some parameters searched
URL = 'https://en.wikipedia.org/wiki/Nematode'

# start a headless broswer
browser = mechanicalsoup.Browser()

# load the page at the URL provided
page = browser.get(URL)

# diagnostics, should print 200.
print(page)
print(page.soup.prettify())

# # Postings all seem to be of this class
# postings = page.soup.find_all("div", class_="job-item job-item-posting")

# for post in postings:
#     # print(post.prettify())
#     text = post.text
#     # if the word bishop appears
#     if text.lower().count('bishop'):
#         # print(post.prettify())
#         # the test includes lots of whitespace and blank lines, so we skip them
#         # print(text.splitlines())
#         for line in text.splitlines():
#             # some lines are not empty, but only contain whitespace
#             # also skip the bookmark and view details links
#             if line.strip() and line.lower() not in ['bookmark', 'view details']:
#                 print(line)

#         # Make a link that can be followed
#         headers = post.select('h3')
#         for header in headers:
#             links = header.find_all('a', href=True)
#             for link in links:
#                 print('https://careers.kccd.edu/' + link['href'])
