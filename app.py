from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/gifs')
def gifs():
    myGifs = [
        "https://media.tenor.com/_YtZdkhPY-AAAAAM/cadeyup.gif",
        "https://media1.tenor.com/m/zC_7Z4G5DYQAAAAd/bluespringjune-txt.gif",
        "https://media1.tenor.com/m/aOA3lIif4wsAAAAd/txt-soobin.gif",
        "https://media.tenor.com/c9VN1l4Kl7EAAAAM/zb1-zhang-hao.gif",
        "https://media.tenor.com/ejjMTBbVsgwAAAAM/ricky-zb1.gif"
        ]
    return render_template('gifs.html', random=random.choice(myGifs), randomBool=False, myGifs=myGifs)

@app.route('/input', methods=['GET', 'POST'])
def input():
    imgData = {
        "dog" : ["https://www.vets4pets.com/siteassets/species/dog/puppy/puppy-sleeping-by-food-bowl.jpg?w=585&scale=down",
                 "https://cdn.britannica.com/71/234471-050-093F4211/shiba-inu-dog-in-the-snow.jpg",
                 "https://nationaltoday.com/wp-content/uploads/2022/08/18-National-Welsh-Corgi-Day-1200x834.jpg",
                 "https://cdn.britannica.com/87/235887-050-3B77621F/Samoyed-dog-mother-with-puppies.jpg",
                 "https://www.akc.org/wp-content/uploads/2017/11/Golden-Retriever-Puppy.jpg"],
        "cat" : ["https://cdn.britannica.com/34/235834-050-C5843610/two-different-breeds-of-cats-side-by-side-outdoors-in-the-garden.jpg",
                 "https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg",
                 "https://as2.ftcdn.net/v2/jpg/02/55/81/17/1000_F_255811711_MaM8Y9ppXidnanreDdDPmE6FXIOq0TED.jpg",
                 "https://d.newsweek.com/en/full/2226604/calico-kitten.jpg?w=1600&h=1600&q=88&f=0db28408ec18dc1011fb75ca3fd17f1c",
                 "https://cats.com/wp-content/uploads/2021/02/PersianFriendlyCatBreeds.jpg"],
        "sheep" : ["https://modernfarmer.com/wp-content/uploads/2017/12/Funny-Sheep-Facts-1200x800.jpg",
                 "https://media.4-paws.org/4/d/5/7/4d579ac34a8ee834f2c9acc26c4eaba336d7f034/shutterstock_97268789%20-%20lamb%20looking%20at%20camera%20-%20web%20size-1277x884.jpg",
                 "https://t4.ftcdn.net/jpg/04/26/13/37/360_F_426133768_JSMZn6XP0bMKCGR6USphfkFhPn7UQKda.jpg",
                 "https://cdn.minnesotamonthly.com/wp-content/uploads/sites/85/2020/04/baby1.jpg",
                 "https://i.pinimg.com/736x/c9/3f/d2/c93fd2167df8c79f88edda37ed3996ba.jpg"],
        "cow" : ["https://a-z-animals.com/media/2022/11/shutterstock_1728214024-1024x681.jpeg",
                 "https://mymodernmet.com/wp/wp-content/uploads/2017/10/highland-cattle-calves-17.jpg",
                 "https://i.pinimg.com/originals/ee/20/ae/ee20ae9fc5e4df4fb7a9d46bc67c5388.jpg",
                 "https://64.media.tumblr.com/41e3ddb34808ba0176f01537c944bded/a8a173ad39cd5b61-a8/s1280x1920/5908bd99697f1638ad3f9cfcb4a0b3b5beac4e41.jpg",
                 "https://media.istockphoto.com/id/932059170/photo/black-angus-calf-close-up.jpg?s=612x612&w=0&k=20&c=M_UyZCzPvgbYhxUnxgIK6reaEHNtphWjoPB5TE8yg0Y="],
        "duck" : ["https://www.kalmbachfeeds.com/cdn/shop/articles/two-white-ducks-in-grass.jpg?v=1706873608",
                 "https://www.peta.org/wp-content/uploads/2016/06/iStock_000015316532_thierry-vialard-602x399.jpg",
                 "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/fluffy-duckling-scott-lyons.jpg",
                 "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Mallard2.jpg/640px-Mallard2.jpg",
                 "https://www.birdspot.co.uk/wp-content/uploads/2022/07/duck-ducklings.jpg"],
        "bear" : ["https://www.biologicaldiversity.org/assets/img/species/mammals/GrizzlyBearRobinSilver.jpg",
                 "https://i.pinimg.com/474x/2e/23/96/2e2396b2217ead38627ae04616a96544.jpg",
                 "https://nhpbs.org/wild/images/brownbearusfwstevehilldebrand1.jpg",
                 "https://wildlife.ca.gov/Portals/0/Images/Game/BlackBear/black-bear_AdobeStock_403065323.jpg?ver=2022-09-02-110300-707",
                 "https://good-nature-blog-uploads.s3.amazonaws.com/uploads/2023/05/1920x910-Blog-Header-1-3-1.jpg"],
    }
    if request.method == 'POST':
        query = request.form['query']
        if query in imgData.keys():
            return render_template('input.html', url=url_for('input'), imgData=imgData[query])
        else:
            return "We do not have images in our database for " + query + " yet."
    return render_template('input.html',url=url_for('input'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)