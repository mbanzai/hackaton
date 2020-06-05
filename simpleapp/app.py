from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26383-1381845104-25.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26358-1381845043-13.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-25329-1381845415-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-23859-1381845509-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19708-1381845008-7.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-19667-1381844937-10.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-3391-1381844336-26.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "http://www.catshaming.co.uk/wp-content/uploads/2014/11/anigif_enhanced-buzz-27162-1381845360-0.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/3.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/1.gif",
    "https://66.media.tumblr.com/133c423fd39ca03fda132071d82d8693/tumblr_n0j8isqnIq1si7ew2o1_400.gifv",
    "https://66.media.tumblr.com/1641e08473c7df8a56d52de2e5c55219/tumblr_nbtr8twYCL1qbxi45o1_500.gifv",
    "https://66.media.tumblr.com/19f67e90f04dbe57f52677076d742522/tumblr_n61npz36HJ1svxaato1_250.gifv",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/45.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/38.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
