# image_search_engine
Selenium based scrapper for collection and flask Api for searching images (image search engine)

install the dependencies in requirement files .

scrappning_code.py is for crawling the images from the website.

after crawling images keep them all images folder in static folder and run the following command for indexing

python index.py --dataset static/images --index index.csv


it will generate the index file.

after that you have to run app.py and in browser write 127.0.0.1:5000

it will run.
