from flask import Flask
from .config import Config
from .models import db, ma, Blog
from .routes import init_routes  # Change this line to import the function
from sqlalchemy import text
blogs = [
    Blog(title='Hemis Monastery', author='Skarma', content='Hemis is a village in the Leh district of Ladakh...Location: Located about 45 kilometers (28 miles) from Leh, Hemis Monastery is one of the largest and richest monasteries in Ladakh. Features: Founded in the 17th century, the monastery is dedicated to Lord Padmasambhava and is famous for its annual Hemis Festival, which celebrates the birth of Padmasambhava with vibrant music, dance, and rituals. Architecture: The monastery is known for its stunning architecture, with colorful murals, intricate woodwork, and a large statue of Guru Padmasambhava. Activities: Visitors can explore the monastery, participate in the festivals, and enjoy the serene surroundings that offer views of the Indus Valley',
         image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvGnC_3Ic-1KpWiN-jtC4jZFHFhBZdZoStgw&s'),
    Blog(title='Stok Trek', author='Skarma', content='Situated about 15 kilometers (9 miles) from Leh, Stok Monastery is part of the Stok Palace complex. Features: The monastery is a center of the Drukpa sect of Tibetan Buddhism and houses a collection of ancient relics, thangkas (traditional Tibetan scroll paintings), and scriptures. Cultural Significance: Stok is also known for its historical importance, as it was once the royal residence of the Namgyal dynasty. The annual Stok Guru Tsechu Festival attracts many visitors. Access: The monastery offers easy access to trekking routes, including those leading to the Stok Kangri mountain, popular among trekkers and climbers.',
         image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwjH4o0M9vf7RwD3XwEGIUfrLThvDSEqMPpw&s'),
    Blog(title='Pangong Tso', author='Skarma', content='An endorheic lake in the Himalayas. Location: Situated at an altitude of about 4,350 meters (14,270 feet), Pangong Lake is approximately 160 kilometers (99 miles) from Leh, the capital of Ladakh.Features: Known for its stunning blue waters that change color throughout the day, the lake is about 134 kilometers (83 miles) long, with a significant portion (about two-thirds) of it lying in China.Activities: Popular for camping, photography, and witnessing the breathtaking views of the surrounding mountains. The area is also famous for its unique wildlife, including migratory birds.Access: The lake can be accessed via a scenic drive through the Chang La Pass, one of the highest motorable roads in the world.',
         image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZRbOxQ609Yj7aae4j-IhGjNWeNwXkihiHag&s'),
    Blog(title='Magnetic-Hill', author='Skarma', content='A cyclops hill where vehicles defy gravity Magnetic Hill is a place where the laws of gravity seem to be defied, giving visitors an illusion of vehicles moving uphill without any power.This intriguing phenomenon, often attributed to an optical illusion or magnetic forces, attracts thousands of visitors each year. Located near Leh in Ladakh, the hill provides a surreal experience against the backdrop of breathtaking landscapes, making it a must-visit spot in Northern India. Whether its the science or the mystery that fascinates you,Magnetic Hill is a captivating destination that blends natural beauty with curious physics',
         image_url='https://media1.thrillophilia.com/filestore/552g4i6pn5c2ggzy6ygnapbk23aw_shutterstock_425389177.jpg'),
    Blog(title='Nubra Valley', author='Skarma', content='A popular attraction in the Himalayas...	Location: Situated north of Leh, Nubra Valley lies at the confluence of the Shyok and Nubra rivers, and it is accessed via the Khardung La Pass, one of the highest passes in the world.Features: Known for its unique landscapes, Nubra is a cold desert featuring sand dunes, lush green valleys, and snow-capped mountains. It is famous for the double-humped Bactrian camels that roam the sand dunes of Hunder.Activities: Popular activities include camel rides, trekking, and visiting the monasteries of Diskit and Hunder. The Diskit Monastery, with its giant statue of Maitreya Buddha, is a key attraction.Culture: Nubra Valley is a cultural melting pot, with influences from Tibetan and Central Asian traditions.',
         image_url='https://www.authenticindiatours.com/app/uploads/2022/04/Bactrian-Camels-Nubra-Valley-Nubra-Jammu-and-Kashmir-1400x550-c-default.jpg'),
    Blog(title='Zanskar Trek', author='Skarma', content='Wonderful walk on frozen surface of Zanskar...Location: Located in the northern Indian state of Jammu and Kashmir, Zanskar is a remote region accessible mainly during the summer months. Features: Famous for its dramatic landscapes, Zanskar Valley is known for its deep gorges, high mountain passes, and vibrant Buddhist culture. The Zanskar River runs through the valley, which is a popular destination for trekking and river rafting. Activities: Trekkers often visit during the summer to explore the beautiful landscapes, while in winter, the frozen river becomes the “Chadar Trek,” attracting adventurers from around the globe. Culture: The valley is home to several ancient monasteries, including Phugtal Monastery and Zangla Monastery, which offer insights into Tibetan Buddhism.',
         image_url='https://www.ladakh-tourism.net/wp-content/uploads/2021/07/zangla-zanskar-1024x536.jpeg'),
    Blog(title='Siachen', author='Skarma', content='Siachen is the second-longest glacier...Location: Situated in the eastern Karakoram range in the Himalayas, Siachen is known as the highest battlefield in the world, located at an altitude of around 5,753 meters (18,875 feet). Features: Spanning over 70 kilometers (43 miles), the glacier is a source of the Nubra River. The region is characterized by harsh weather conditions and is covered with snow year-round. Activities: Due to its strategic military importance, access to Siachen is restricted. However, it is a significant area for scientific research and adventure expeditions. Military Presence: The glacier has been a site of military conflict between India and Pakistan since the 1980s, making it one of the most challenging places for soldiers due to extreme cold and altitude.',
         image_url='https://i0.wp.com/greenverz.com/wp-content/uploads/2023/03/shutterstock-1702720045.webp?fit=1320%2C873&ssl=1'),
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    init_routes(app)  # Initialize routes

    with app.app_context():
        db.create_all()  # Create database tables

        # Clear existing data
        db.session.execute(text('DELETE FROM blogs;'))

        # Insert sample blog data
        for blog in blogs:
            existing_blog = Blog.query.filter_by(title=blog.title).first()
            if not existing_blog:
                db.session.add(blog)

        db.session.commit()
        print("Sample data inserted successfully!")

    return app
