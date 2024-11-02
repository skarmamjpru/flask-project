
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

blogs = [
    {'id': 1, 'title': 'Magnetic Hill', 'author': 'Skarma',
        'content': '''A cyclops hill where vehicles defy gravity Magnetic Hill is a place where the laws of gravity seem to be defied, giving visitors an illusion of vehicles moving uphill without any power. 
        This intriguing phenomenon, often attributed to an optical illusion or magnetic forces, attracts thousands of visitors each year. Located near Leh in Ladakh, the hill provides 
        a surreal experience against the backdrop of breathtaking landscapes, making it a must-visit spot in Northern India. Whether it's the science or the mystery that fascinates you, 
        Magnetic Hill is a captivating destination that blends natural beauty with curious physics.''', 'image': 'https://media1.thrillophilia.com/filestore/552g4i6pn5c2ggzy6ygnapbk23aw_shutterstock_425389177.jpg'},
    {'id': 2, 'title': 'Hemis Monastery', 'author': 'Skarma',
        'content': '''Hemis is a village in the Leh district of Ladakh, India, known for its monastery, national park, and annual festival Hemis Monastery, located in the picturesque Leh district of Ladakh, is one of the region’s most revered cultural and spiritual centers. Founded in the 17th century, this Tibetan Buddhist monastery is known for its striking architecture, large gold-plated statue of Guru Padmasambhava, and stunning murals depicting various deities. Hemis hosts the annual Hemis Festival, celebrated in honor of Guru Padmasambhava, where monks perform sacred masked dances, or cham, that symbolize the triumph of good over evil. Beyond the spiritual ambiance, visitors are also drawn to the Hemis National Park, which shelters the rare and elusive snow leopard. ''', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvGnC_3Ic-1KpWiN-jtC4jZFHFhBZdZoStgw&s'},
    {'id': 3, 'title': 'Siachen', 'author': 'Skarma',
        'content': '''Siachen is the second-longest glacier within Earth’s midlatitudes Stretching over 76 kilometers, Siachen Glacier is the second-longest glacier outside the polar regions and a unique point of human endurance and exploration. Nestled in the rugged Karakoram Range, Siachen lies at the border between India and Pakistan. Despite the harsh conditions with temperatures dropping to extreme lows, the glacier is an active zone due to its strategic significance. Beyond its geopolitical importance, the glacier offers scientists insights into climate and glacial dynamics and provides a stunning yet forbidding environment for mountaineers. The icy terrain and sheer remoteness make Siachen a formidable yet fascinating landmark.''', 'image': 'https://i0.wp.com/greenverz.com/wp-content/uploads/2023/03/shutterstock-1702720045.webp?fit=1320%2C873&ssl=1'},
    {'id': 4, 'title': 'Pangong Tso', 'author': 'Skarma',
        'content': '''An endorheic lake in the Himalayas thats a must-see Pangong Tso is a breathtaking endorheic lake situated in the Himalayas at an altitude of about 4,350 meters. Known for its stunning blue hues, Pangong stretches 134 kilometers and spans both India and China, making it an international wonder. This lake is famous for its changing colors, shifting from shades of blue to green to red depending on the time of day and weather. A major attraction for travelers in Ladakh, Pangong Tso gained widespread fame after being featured in the Bollywood film 3 Idiots, and it remains a bucket-list destination for adventure seekers and nature enthusiasts alike.''', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZRbOxQ609Yj7aae4j-IhGjNWeNwXkihiHag&s'},
    {'id': 6, 'title': 'Nubra Valley', 'author': 'Skarma',
        'content': '''A popular attraction in the Himalayas where you can camp, stargaze, and ride a jeep across the dunes Nubra Valley is a serene and scenic destination in the northern part of Ladakh, offering a blend of natural beauty and unique cultural experiences. Known for its vast landscapes of sand dunes, Nubra Valley is home to the rare double-humped Bactrian camels, which add to the valley’s mystique. Here, visitors can camp under star-lit skies, enjoy jeep rides across the dunes, and visit ancient monasteries like Diskit, which hosts a towering statue of Maitreya Buddha. The valley is often referred to as the “Valley of Flowers” for its burst of color in the summer months, making it an oasis of beauty amid Ladakh’s rugged terrain.''', 'image': 'https://www.authenticindiatours.com/app/uploads/2022/04/Bactrian-Camels-Nubra-Valley-Nubra-Jammu-and-Kashmir-1400x550-c-default.jpg'},
    {'id': 5, 'title': 'Zanskar Trek', 'author': 'Skarma',
        'content': '''Wonderful walk on frozen surface of Zanskar...full of adventure, thrill and fun. The Zanskar Trek, also known as the “Chadar Trek” during winter, is a thrilling adventure over the frozen Zanskar River. This challenging trek takes adventurers through narrow gorges, over ice-covered pathways, and past ancient caves and villages isolated in the harsh winter months. Trekkers witness the frozen waterfalls, breathtaking views, and a pristine, untouched landscape. During the warmer months, the region becomes accessible by foot or vehicle, allowing visitors to explore the Zanskar Valley’s Buddhist monasteries, green villages, and tranquil rivers. Known for its extreme conditions, the Zanskar Trek is a favorite among seasoned trekkers and thrill-seekers.
''', 'image': 'https://www.ladakh-tourism.net/wp-content/uploads/2021/07/zangla-zanskar-1024x536.jpeg'},

]


@app.route('/')
def home():
    return render_template('home.html', title='Home', blogs=blogs)


@app.route('/account')
def account():
    return render_template('account.html', title='Account', user={'name': 'Skarma', 'bio': 'M.Tech'})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = next((b for b in blogs if b['id'] == blog_id), None)
    return render_template('blog_detail.html', blog=blog) if blog else "Blog not found", 404


@app.route('/search')
def search():

    query = request.args.get('query')
    if query:
        search_results = [
            blog for blog in blogs if query.lower() in blog['title'].lower()]
    else:
        search_results = []

    return render_template('home.html', title='Search Results', blogs=search_results)


if __name__ == '__main__':
    app.run(debug=True)
