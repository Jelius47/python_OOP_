import re 


urls="""
hello kindly Recive these urls
2025-05-20
http://jelius-render_portfolio.com
https://www.python-engineer.com
http://www.pyeng.net"""

pattern = re.compile(r"https?://(www\.)?([a-zA-z-]+)(\.[a-zA-Z]+)")
web_urls = pattern.finditer(urls)
for match in web_urls:
    print(match)

# Substituting the urls to get clean urls 

# This is where group actual start to matter forinstance one needs to replace 
# http or https and keep the other side of url as it is 

subed_urls = pattern.sub(r"\2\3",urls)# This is to refer the two groups created in our pattern
print(subed_urls)


# Lastly when we want to search for the letter that we are not sure of its case 

pattern_ = re.compile(r"recive",re.IGNORECASE)# Also you can use re.I it ill just work as usual

matches_ = pattern_.finditer(urls)

for match in matches_:
    print("\n"+ match.group())