# Movie Trailer Website

This project dynamically generates an HTML file for a movie trailer website using a Python data structure.  The website displays the movie title and box art.  The movie trailer will play once the box art is clicked. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

- Python 2.7
- Download source code `entertainment_center.py`, `fresh_tomatoes.py`, and `media.py` and save all three to a single folder on your local machine.  The source code can be found [here](https://github.com/JakeTux8/Movie-Trailer-Website.git)

### Creating Webpage 

To create the HTML file for the web page, do the following:

- Ensure that all three modules, `entertainment_center.py`, `fresh_tomatoes.py`, and `media.py` are located in the same folder. 
- Using Python 2.7, run the entertainment_center.py module:

`$ python entertainment_center.py`

&emsp; &emsp; &emsp; - **Note**: The movie objects and array in the entertainment_center.py module can be modified as needed.

### Modules

The **`media.py`** module contains the Movie class.  The Movie class has 5 attributes:  4 object variables and 1 class method. 
```
self.title
self.storyline
self.poster_image_url
self.trailer_youtube_url

function show_trailer()
```

When a Movie object is created, it takes 4 strings as arguments.

- The first  string is the `"movie title"`
- The second string is the `"synopsis of the movie"`
- The third string is the `"url for the poster image for the movie"`
- The fourth string is the `"url for the youtube movie trailer"`

The `show_trailer()` method opens the youtube url provided when the Movie object is created. 

The **`fresh_tomatoes.py`** module takes an array of Movie objects as an argument and dynamically creates an HTML file for the movie trailer website, then opens the HTML file in the local machine's default web browser.

 The **`entertainment_center.py`** is where the Movie objects are created.  The an array of the Movie objects are created, and then passed to the `fresh_tomatoes.py` module to create the movie trailer website HTML file and open the file in the local machine's default web browser.
 

## Acknowledgements

The code for the `fresh_tomatoes.py` module was provided by the awesome staff at Udacity.  Thanks for the help guys! 
