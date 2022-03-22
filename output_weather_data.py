#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
# print HTTP header
print ("Content-type: text/html\n\n")

# open file with data from script
datafile = open("/home/pi/linda_proj/current_weather.txt", "r")
page_data = datafile.read()
datafile.close()

# define an HTML template
page_str = """<!DOCTYPE html>
<html>
    <head>
        <title>My weather</title>
    </head>
    <body>
        <h1>My current weather conditions </h1>
        {data}
    </body>
</html>"""

# format and print the page
print (page_str.format (data = page_data))
