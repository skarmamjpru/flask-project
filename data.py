# seed_data.py
from app import db, Blog, app  # Import your app to use the app context

# Define sample blog data
blogs = [
    Blog(title='Magnetic Hill', author='Skarma', content='A cyclops hill where vehicles defy gravity...',
         image_url='https://media1.thrillophilia.com/filestore/552g4i6pn5c2ggzy6ygnapbk23aw_shutterstock_425389177.jpg'),
    Blog(title='Hemis Monastery', author='Skarma', content='Hemis is a village in the Leh district of Ladakh...',
         image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvGnC_3Ic-1KpWiN-jtC4jZFHFhBZdZoStgw&s'),
    Blog(title='Siachen', author='Skarma', content='Siachen is the second-longest glacier...',
         image_url='https://i0.wp.com/greenverz.com/wp-content/uploads/2023/03/shutterstock-1702720045.webp?fit=1320%2C873&ssl=1'),
    Blog(title='Pangong Tso', author='Skarma', content='An endorheic lake in the Himalayas...',
         image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZRbOxQ609Yj7aae4j-IhGjNWeNwXkihiHag&s'),
    Blog(title='Nubra Valley', author='Skarma', content='A popular attraction in the Himalayas...',
         image_url='https://www.authenticindiatours.com/app/uploads/2022/04/Bactrian-Camels-Nubra-Valley-Nubra-Jammu-and-Kashmir-1400x550-c-default.jpg'),
    Blog(title='Zanskar Trek', author='Skarma', content='Wonderful walk on frozen surface of Zanskar...',
         image_url='https://www.ladakh-tourism.net/wp-content/uploads/2021/07/zangla-zanskar-1024x536.jpeg'),
]

# Insert data within the app context
with app.app_context():
    db.create_all()  # Ensure all tables are created
    db.session.add_all(blogs)  # Add the sample blogs to the session
    db.session.commit()  # Commit to save to the database
    print("Sample data inserted successfully!")
