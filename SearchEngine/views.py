# from SearchEngine.search import google
import pycurl
from django.shortcuts import render, redirect

from io import BytesIO


def foo():
    """simple doc"""


def homepage(request):
    return render(request, 'home.html')


def results(request):
    if request.method == "POST":
        search = request.POST['search']
        print(search)

        b_obj = BytesIO()
        crl = pycurl.Curl()

        # Set URL value
        crl.setopt(crl.URL, 'search')

        # Write bytes that are utf-8 encoded
        crl.setopt(crl.WRITEDATA, b_obj)

        # Perform a file transfer
        crl.perform()

        # End curl session
        crl.close()

        # Get the content stored in the BytesIO object (in byte characters)
        get_body = b_obj.getvalue()

        # Decode the bytes stored in get_body to HTML and print the result
        print('Output of GET request:\n%s' % get_body.decode('utf8'))

    else:
        return redirect('/')
