from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
	__tablename__="products"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	price=Column(Integer)
	picture_link=Column(String)
	description=Column(String)
	review=Column(String)
	product_num=0
	product_number= product_num=+1

class Cart(Base):
	__tablename__="cart"
	id=Column(Integer, primary_key=True)
	productID=Column(Integer)
	product_num=Column(Integer)
	product_num=0
	product_number= product_num=+1
# class shipping(Base):
# 	__tablename__="total_w_shipping"
# 	id=Column(Integer,primary_key=True)
# 	next_day=5
# 	standard=2
# 	personal=0