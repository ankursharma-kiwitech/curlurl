# # import docs as docs
# # import requests
# # from bs4 import BeautifulSoup
#
# # done
# # def google(s):
# #     links = []
# #     text = []
# #     USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
# #     headers = {"user-agent": USER_AGENT}
# #     r = requests.get("https://www.google.com/search?q=" + s, headers=headers)
# #     soup = BeautifulSoup(r.content, "html.parser")
# #     for g in soup.find_all('div', class_='yuRUbf'):
# #         a = g.find('a')
# #         t = g.find('h3')
# #         links.append(a.get('href'))
# #         text.append(t.text)
# #     return links, text
# #
#
# # Somethime request.code == 500
# import pycurl
# import io
# import re
# import pycurl
# from io import StringIO
#
#
# # def curl(url):
# #     buffer = StringIO()
# #     url = 'https://docs.djangoproject.com/en/3.0/ref/request-response/'
# #     c = pycurl.Curl()
# #     c.setopt(c.URL, url)
# #     c.setopt(c.WRITEDATA, buffer)
# #     c.perform()
# #     c.close()
# #     body = buffer.getvalue()
# #     return body
#
# # if __name__ == "__main__":
# #     header = StringIO()
# #     body = StringIO()
# #     curl = pycurl.Curl()
# #
# #     # curl.setopt(pycurl.HEADERFUNCTION, header.write)
# #     # curl.setopt(pycurl.WRITEFUNCTION, body.write)
# #     curl.setopt(pycurl.URL, "http://www.python.org/")
# #
# #     curl.perform()
# #     print(body.getvalue())
# #     print(header.getvalue())
# #     curl.close()
# #     return body.getvalue(), header.getvalue()
#
# def curl(request):
#     buffer = StringIO()
#     url = 'https://docs.djangoproject.com/en/3.0/ref/request-response/'
#     c = pycurl.Curl()
#     c.setopt(c.URL, url)
#     c.setopt(c.WRITEDATA, buffer)
#     c.perform()
#     c.close()
#     body = buffer.getvalue()
#     return curl(url)
#
# # write a code to find te country name from the latitude and longitude
# def get_country_from_lat_long(lat, long,request):
#     lat=request.GET.get('lat')
#     long=request.GET.get('long')
#     url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + long + '&key=AIzaSyD0C4hD4H4_y-_P-_g5_5-_H5_Z_0-_P-_'
#     print(url)
#     return curl(url)