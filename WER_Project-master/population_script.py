import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","WER_project.settings")

import django
django.setup()
from WER_app.models import Review, Page
from django.core.files import File
import os
import glob

"""
Review entity template
[
        {"title":"title",
         "comment":,
         "price":,
         "quality":,
         "atmosphere":,}]
"""

#populates the database with reviews for resteraunts
def populate():
    cwd = os.getcwd()
    files = glob.glob(cwd+'/media/restaurant/*')
    for f in files:
        os.remove(f)
    
    Paesano_Pizza = [{"title":"Paesano Pizza",
         "comment":"Busy place but fast service with delicious pizza with a perfect thing crust. Quite loud but great if that is your kind of atmosphere.",
         "price":4,
         "quality":5,
         "atmosphere":4 },
         {"title":"Paesano Pizza",
         "comment":"Friendly staff",
         "price":5,
         "quality":5,
         "atmosphere":5},
         {"title":"Paesano Pizza",
         "comment":"Took ages to get a table and my wife's pizza had mushroom on it by accident when she is allergic!! I won't be coming back anytime soon.",
         "price":2,
         "quality":3,
         "atmosphere":2},]
    Ubiquitous_Chip = [{"title":"Ubiquitous Chip",
         "comment":"Fancy and very nice",
         "price":4,
         "quality":5,
         "atmosphere":4},
         {"title":"Ubiquitous Chip",
         "comment":"Good food but pretentious name",
         "price":3,
         "quality":5,
         "atmosphere":2},
         {"title":"Ubiquitous Chip",
         "comment":"Food was subpar but the name was very interesting",
         "price":3,
         "quality":2,
         "atmosphere":3}]
    Food_for_Thought = [
        {"title":"Food for Thought",
         "comment":"Not enough seating overall, but nice food and a relaxing place to take a break from doing work.",
         "price":4,
         "quality":4,
         "atmosphere":4},
         {"title":"Food for Thought",
         "comment":"There was no cheese and ham sandwich it was a cheese sandwich or a ham sandwich and I wan't both.",
         "price":3,
         "quality":1,
         "atmosphere":2},
         {"title":"Food for Thought",
         "comment":"Convenient",
         "price":5,
         "quality":5,
         "atmosphere":5}]
    Food_to_Go = [
        {"title":"Food to Go",
         "comment":"Very nice and excellent sandwiches.",
         "price":4,
         "quality":4,
         "atmosphere":5},
         {"title":"Food to Go",
         "comment":"Convenient and good food.",
         "price":4,
         "quality":4,
         "atmosphere":5},
         {"title":"Food to Go",
         "comment":"Not very interesting",
         "price":4,
         "quality":3,
         "atmosphere":2},
         {"title":"Food to Go",
         "comment":"Really useful if you need food to go.",
         "price":3,
         "quality":4,
         "atmosphere":3}]
    Cafe_Piccolino = [
        {"title":"Cafe Piccolino",
         "comment":"Friendly and helpful staff",
         "price":4,
         "quality":4,
         "atmosphere":3},
         {"title":"Cafe Piccolino",
         "comment":"My grandson Freddie brought me here today as I am visiting him from Edinburgh, it was so nice to spend time with him and talk to him over lunch. Toastie a bit cold but my heart was warm and happy.",
         "price":4,
         "quality":3,
         "atmosphere":4}]
    Food_in_Focus = [
         {"title":"Food in Focus",
         "comment":"Friendly and helpful staff",
         "price":4,
         "quality":4,
         "atmosphere":3}]
    Food_Factory = [{"title":"Food Factory",
         "comment":"Lovely",
         "price":4,
         "quality":4,
         "atmosphere":5}]
    G12_Cafe = [{"title":"G12 Cafe",
         "comment":"Nice",
         "price":4,
         "quality":4,
         "atmosphere":5}]
    The_Union_Kitchen = [{"title":"The Union Kitchen",
         "comment":"Great",
         "price":4,
         "quality":4,
         "atmosphere":5}]
    Bar_Kitchen = [{"title":"Bar Kitchen",
         "comment":"Lovely",
         "price":4,
         "quality":4,
         "atmosphere":5}]
         
    MacTassos = [{"title":"MacTassos",
         "comment":"Friendly",
         "price":4,
         "quality":4,
         "atmosphere":5}]
    The_Left_Bank = [{"title":"The Left Bank",
         "comment":"Friendly",
         "price":4,
         "quality":4,
         "atmosphere":5}]
    
    #adds resteraunts to the database with all of the required info to create a page
    reviews = {"Paesano Pizza": {"pages": Paesano_Pizza, "image":"Paesano_Pizza.jpg", "description":"Pizza Place", "address":"471 Great Western Road, Glasgow G12 8HL, Scotland", "openingHours":"Sun - Wed  12:00 - 22:30\nThu 12:00 - 23:00\nFri12:00 - 00:00", "onCampus":False, "latitude":55.875172, "longitude":-4.2839027},
                "Ubiquitous Chip": {"pages": Ubiquitous_Chip, "image":"Ubiquitous_Chip.jpg", "description":"Artistic brasserie dishes that display their provenance, served in a leafy space with fairy lights.", "address":"12 Ashton Lane, Glasgow G12 8SJ, Scotland", "openingHours":"Sun – Sat 11:00 - 01:00", "onCampus":False, "latitude":55.874893, "longitude":-4.2954117},
                "Food for Thought": {"pages": Food_for_Thought, "image":"Library_Cafe.jpg", "description":"Cafe in the Fraser Building for students, staff and visitors to the campus, serving hot meals and snacks.", "address":"Fraser Building, 65 Hillhead St, Glasgow G12 8QF", "openingHours":"Mon-Fri 11:00 - 15:00 ","onCampus":True, "latitude":55.8731782, "longitude":-4.2905351},
                "Food to Go": {"pages": Food_to_Go, "image":"Food_for_Thought.jpg", "description":"Offers everything you need for breakfast on the go, lunch on the run or an eveningsnack to sustain you during late study sessions.", "address":"Fraser Building, 65 Hillhead St, Glasgow G12 8QF", "openingHours":"Mon-Thu 08:00 - 18:00, Fri 08:00 - 16:30", "onCampus":True, "latitude":55.8733697, "longitude":-4.2911344},
                "Cafe_Piccolino": {"pages": Cafe_Piccolino, "image":"Cafe_Piccolino.jpg", "description":"Proud to serve Orang Utan coffee supporting an important Sumatran conservation project", "address":"Ashton Ln, Glasgow G12 8QR", "openingHours":"Mon-Fri 08:30 - 15:00 ", "onCampus":True, "latitude":55.8733697, "longitude":-4.2911344},
                "Food in Focus": {"pages": Food_in_Focus, "image":"Food_in_Focus.jpg", "description":"Comfy seating in a newly decorated area for library users and vending machines accessible during library opening hours", "address":"University of Glasgow, Hillhead St, Glasgow G12 8QE", "openingHours":"Mon- Thu: 10:00 - 20:00\nFri: 10:00 - 17:00\nSat/Sun: 10:30 - 17:00", "onCampus":True, "latitude":55.8733697, "longitude":-4.2911344},
                "Food Factory": {"pages": Food_Factory, "image":"Food_Factory.jpg", "description":"The Queen Margaret Union is the one of four students' unions at the University of Glasgow, Scotland. Founded in 1890, it caters to the social and cultural needs of its members by providing a range of services including entertainment, catering, shop facilities, bars and games.", "address":"22 University Gardens, Glasgow G12 8QN", "openingHours":"Mon - Fri 08:00 - 22:00", "onCampus":True, "latitude":55.8727845, "longitude":-4.2958293},
                "G12 Cafe": {"pages": G12_Cafe, "image":"G12_Cafe.jpg", "description":"G12,  the glass fronted Café/Bar running along University Avenue. G12 will offer a unique environment completely different to anything on offer at GUU.", "address":"42 University AveGlasgow G12 8NN", "openingHours":"Mon - Sun 08:00 - 23:00", "onCampus":True, "latitude":55.8737468, "longitude":-4.2936335},
                "The Union Kitchen": {"pages": The_Union_Kitchen, "image":"The_Union_Kitchen.jpg", "description":"The Servery will never dissapoint students looking for a quick breakfast or a hearty meal. Serving breakfast till 11am and lunch thereafter, The GUU Servery provides the best value for money catering on campus.", "address":"32 University Avenue, Glasgow G12 8LX", "openingHours":"Mon - Fri 08:00 - 23:00, Sat 10:00 - 23:00", "onCampus":True, "latitude":55.8725958, "longitude":-4.2870855},
                "Bar Kitchen": {"pages": Bar_Kitchen, "image":"Bar_Kitchen.jpg", "description":"Located in the heart of the West End of Glasgow, Bank Street Bar Kitchen is a lively bar offering a fantastic range of spirits, craft beers and wines accompanied by some awesome food including our stone baked pizzas, gourmet burgers and delicious curries as well as other adventurous, tasty dishes.", "address":"52 Bank St, Glasgow G12 8LZ", "openingHours":"Mon - Sun 10:00 - 01:00", "onCampus":False, "latitude":55.8731341, "longitude":-4.2864629},
                "MacTassos": {"pages": MacTassos, "image":"MacTassos.jpg", "description":"Authentic Greek Kebab van perfect for Glasgow students", "address":"Kelvin Way, Glasgow G3 7TA, Scotland", "openingHours":"Mon - Sat 11:00 - 17:00", "onCampus":False, "latitude":55.8680642, "longitude":-4.2885773},
                "The Left Bank": {"pages": The_Left_Bank, "image":"The_Left_Bank.jpg", "description":"The left bank is in the heart of Glasgow’s west end, a stone's throw from Kelvingrovepark and just down the hill from the university of Glasgow, the mackintosh house and the Hunterian gallery and museum. We sell delicious home cooking all day starting early with our breakfasts which are recommended by the New York times no less. our light and airy bar and restaurant is well known locally, convenient for anything from a well-made coffee to a soup and sandwich or a table full of our delicious small plates.", "address":"Kelvin Way, Glasgow G3 7TA, Scotland", "openingHours":"Mon - Fri 09:00 - 00:00, Sat - Sun 10:00 - 00:00", "onCampus":False, "latitude":55.872457, "longitude":-4.2849677}}

                 
                 
    for review, review_data in reviews.items():
        for p in review_data["pages"]:
            r = (add_review(p["title"], p["comment"], p["price"], p["quality"], p["atmosphere"]))
        
        add_page(r, p["title"], review_data["image"] , review_data["description"], review_data["address"], review_data["openingHours"], review_data["onCampus"], review_data["latitude"], review_data["longitude"])

        
        
    for r in Review.objects.all(): 
         print(str(r))

    
#a method that adds a review to the database    
def add_review(title, comment, price, quality, atmosphere):
    r = Review.objects.create()
    r.title=title
    r.comment = comment  
    r.price = price
    r.quality = quality
    r.atmosphere = atmosphere
    r.save()
    return r
 
#method that adds a page to the database
def add_page(review, title, image, description, address, openingHours, onCampus, latitude, longitude):
    p = Page.objects.get_or_create(title=title)[0]
    cwd = os.getcwd()
    pic_dir = cwd+'/media/'+image
    p.picture.save(image, File(open(cwd+'/media/'+image, 'rb')))
    p.description = description
    p.address = address
    p.openingHours = openingHours
    p.onCampus = onCampus
    p.latitude = latitude
    p.longitude = longitude
    p.save()

#runs the populate() method
if __name__ == '__main__':
    print("Starting WER_app population script...")
    populate()