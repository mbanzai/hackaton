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
    "http://www.dogshaming.co.uk/wp-content/uploads/2014/11/10976_10152751004061385_6101333622735638035_n.jpg",
    "https://tenor.com/view/funny-dog-gif-7753357",
    "https://media.tenor.com/images/a10e992704a5d395217800f925391da9/tenor.gif",
    "https://tenor.com/view/turtle-animals-animated-save-the-turtle-dog-gif-15349938",
    "https://post.barkbox.com/?attachment_id=1561",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/3.gif",
    "https://s3.amazonaws.com/barkpost-assets/50+GIFs/1.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
