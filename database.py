from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# def createThread():
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
	# return session

def add_product(name,price,picture_link,description,review):
	product=Product(name=name,price=price,picture_link=picture_link,description=description,review=review)
	session.add(product)
	session.commit()

def add_to_cart_db(product_id):
	cart_product=Cart(productID=product_id)
	session.add(cart_product)
	session.commit()

def edit_by_id(product_id,name,price,link,description,review):
	 p = session.query(Product).filter_by(id=product_id).first()
	 p.name = name
	 p.price = price
	 p.picture_link = link
	 p.description = description
	 p.review = review
	 session.commit()


def delete_by_id(product_id):
	session.query(Product).filter_by(id=product_id).delete()
	session.commit()

def delete_all_cart_db():
	session.query(Cart).delete()
	session.commit()


def return_all():
	products = session.query(Product).all()
	return products

	
def return_by_id(product_id):
	product = session.query(Product).filter_by(id=product_id).one()
	return product


# add_product("PIG BEBE",3,"/static/images/temp/p10.jpg","we all PIGS at the end of the day","4.4(5250)")
# add_product("WTF",4,"/static/images/temp/p12.jpg","when you don't know what is happening in your life","4.4(3400)")
# add_product("Loai's legendary sleeping socks",90000,"https://ae01.alicdn.com/kf/HTB1MuhmavfsK1RjSszgq6yXzpXaw.jpg_q50.jpg","BOOTIFOL","5/5(3600)")
# add_product("Cool Club",7,"/static/images/temp/p8.jpg","you can's sit with us","5(4400)")
# add_product("Socariot",2,"/static/images/temp/p6.jpg","for sweet days","4.4(2400)")
# add_product("MARVEL",3,"/static/images/temp/p55.jpg","for a true fan","4.2(3460)")
# add_product("Mixed EMOTION Club",4,"/static/images/temp/p44.jpg","made 4 REAL emotional DESASTERS","4.7(5000)")
# add_product("CREATIVE CREATURE",3,"/static/images/temp/p66.jpg","when you feel artsy","4.4(3200)")
# add_product("CRAZY life",6,"/static/images/temp/p23.jpg","fun days deserve fun socks!","5(5000)")

# def Add_To_Cart(session,product_id):
# 	cart=Cart(product_id)
# 	session.add(Cart)
# 	session.commit()

# add_product("A STAR","$29,999.79","star.jpg","This is a star loai gave me")
