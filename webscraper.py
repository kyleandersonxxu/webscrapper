from urllib.request import urlopen

url1 = "http://olympus.realpython.org/profiles/aphrodite"

web page = urlopen(url1)
html_bytes = web_page.read()
html = html_bytes.decode("utf-8")

print (html)