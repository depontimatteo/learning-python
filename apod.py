import argparse
from datetime import date, timedelta
from random import randint
import os
import urllib.request

def parse_command_line():
    """
    Parse the command line arguments and return the argparse object.
        
    There should be no positional arguments and 4 optional arguments.
    The help message generated by the parser should look like:
    usage: apod.py [-h] [-d month day year] [-s] [-k API_KEY] [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -d month day year, --date month day year
                            formatted date (i.e. 03 28 1998)
      -s, --surprise        select a random date for a surprise image
      -k API_KEY, --api_key API_KEY
                            NASA developer key
      -v, --verbose         verbose mode


    HINT: for the --date optional argument, use a tuple: metavar = ("month", "day", "year")

    args:
        None
        
    returns:
        args: generated argparse object with all the parsed command line arguments      
    """
    
    #TODO: Your code goes here
    pass

def create_date(datelist, surprise):
    """
    Create a valid date object.
    
    If datelist is not an empty list, create a date object using the data in the list [month day year].
    If datelist is empty, and surprise is True, create a random date object between June 16 1995 and today.
    If datelist is empty and surprise is False, create a date object using yesterday's date
    
    If the datelist contain invalid information (i.e. month = 1323), the function should return None
    If the created date is invalid (i.e. earlier than June 16 1995 or later than today), the function should return None
    
    HINTS: 
        - Use exception handling to validate the info in the datelist
        - Use timedelta objects to generate a surprise date
    
    args:
        d: list containing the [month, day, year] or an empty list []
        surprise: Boolean, if True and datelist is empty, generate a random date 
                  the earliest valid date is June 16 1995
    
    returns:
        created valid date object or None when date selected by user is invalid (i.e. in the future)
    """
    
    #TODO: Your code goes here
    pass

    
def query_url(d, api_key):
    """
    Create a URL to fetch an image metadata (not the image itself).
    
    The base URL is https://api.nasa.gov/planetary/apod?
    For a complete URL, the api_key and the date (d) (formatted as YYYY-MM-DD) should be added to the base.
    For example, if date object (d) represents July 5 2016 and api_key is DEMO_KEY, the complete URL is:
    
    https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2016-07-05
    
    HINTS: 
        - Use strftime to format the date object (d) as necessary
    
    args:
        d: date object containing a valid date
        api_key: string containing "DEMO_KEY" or your valid NASA developer key for higher request rate limits
        
    returns:
        complete url as a string
        
    examples:
        d is a date object representing Sep 24 2017
        query_url(d, "DEMO_KEY") ==> returns https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2017-09-24
        
        d is a date object representing Jul 19 1999
        query_url(d, "ABCDEFG") ==> returns https://api.nasa.gov/planetary/apod?api_key=ABCDEFG&date=1999-07-19
    """
        
    #TODO: Your code goes here
    pass


def save_image(d, image):
    """
    Save binary image on disk.
    
    Use the date of the image (d) to create a directory structure (year/month) if it doesn't exist already,
    then save the binary image under its corresponding year and month using the date (d) + '.jpg' as a file name
    
    HINT: Binary data can be written to files in a similar way to how strings are written to files.
          Use 'wb' (write binary) instead of 'w' in the file open clause (i.e. open(file_path, 'wb'))

    args:
        d: date object containing image date
        image: binary image itself
    
    returns:
        file_path: where the image was saved
        
    examples:
        if d = 2017-8-21, the image will be saved as: 2017/8/2017-8-21.jpg
        if d = 1998-4-15, the image will be saved as: 1998/4/1998-4-15.jpg
    """
    
    #TODO: Your code goes here
    pass

    
    
def request(url):
    """
    Download the metadata located at url and return it as a dictionary.
     
    args:
        url: to request image metadata for a specific date
    
    returns:
        dictionary of the metadata downloaded from url
        
    examples:
        if url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2017-09-24"
        url_request(url) ==> returns dictionary:
        
        {
          "copyright": "The League of Lost Causes", 
          "date": "2017-09-24", 
          "explanation": "What is that light in the sky? Perhaps one of humanity's more common questions, an answer may result from a few quick observations.  For example -- is it moving or blinking? If so, and if you live near a city, the answer is typically an airplane, since planes are so numerous and so few stars and satellites are bright enough to be seen over the din of artificial city lights. If not, and if you live far from a city, that bright light is likely a planet such as Venus or Mars -- the former of which is constrained to appear near the horizon just before dawn or after dusk.  Sometimes the low apparent motion of a distant airplane near the horizon makes it hard to tell from a bright planet, but even this can usually be discerned by the plane's motion over a few minutes. Still unsure?   The featured chart gives a sometimes-humorous but mostly-accurate assessment.  Dedicated sky enthusiasts will likely note -- and are encouraged to provide -- polite corrections.   Chart translations: Spanish, Italian, Polish, Tamil, Kannada, Latvian, and Norwegian", 
          "hdurl": "https://apod.nasa.gov/apod/image/1709/astronomy101_hk_750.jpg", 
          "media_type": "image", 
          "service_version": "v1", 
          "title": "How to Identify that Light in the Sky", 
          "url": "https://apod.nasa.gov/apod/image/1709/astronomy101_hk_960.jpg"
        }
        
    """
    
    # request the content of url and save the retrieved binary data
    with urllib.request.urlopen(url) as response:
        data = response.read()
    
    # convert data from byte to string
    data = data.decode('UTF-8')
    
    # convert data from string to dictionary
    data = eval(data)
    return data

def download_image(url):
    """
    Download the image located at url.
    
    args:
        url: where actual image is located
        
    returns:
        image as binary data
    """
    
    # request the content of url and return the retrieved binary image data
    with urllib.request.urlopen(url) as response:
        image = response.read()
    return image

def main():
    # NASA developer key (You can hardcode yours for higher request rate limits!)
    API_KEY = "cZX0zRDveiz7AfGfOW23typMH3NCnS3uvQJc0ZNS"

    # parse command line arguments
    args = parse_command_line()
    
    # update API_KEY if passed on the command line
    print(args.api_key)
    if args.api_key != '':
        API_KEY = args.api_key
    
    # create a request date
    d = create_date(args.date, args.surprise)
    
    # ascertain a valid date was created, otherwise exit program
    if d is None:
        print("No valid date selected!")
        exit()
    
    # verbose mode
    if args.verbose:
        print("Image date: {}".format(d.strftime("%b %d, %Y")))
        
    # generate query url
    url = query_url(d, API_KEY)

    # verbose mode    
    if args.verbose:
        print("Query URL: {}".format(url))
        
    # download the image metadata as a Python dictionary
    metadata = request(url)

    # verbose mode    
    if args.verbose:
        # display image title, other metadata can be shown here
        print("Image title: {}".format(metadata['title']))
    
    # get the url of the image data from the dictionary
    image_url = metadata['url']

    # verbose mode    
    if args.verbose:
        print("Downloading image from:", image_url)
        
    # download the image itself (the returned info is binary)
    image = download_image(image_url)
    
    # save the downloaded image into disk in (year/month)
    # the year and month directories correspond to the date of the image (d)
    # the file name is the date (d) + '.jpg'
    save_image(d, image)

    print("Image saved")

if __name__ == '__main__':
    main()
