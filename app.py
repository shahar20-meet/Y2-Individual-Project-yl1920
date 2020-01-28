from flask import *
from flask import session as login_session
from database import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def home():
	products=return_all() #This line should have all products from the table
	return render_template("index.html", products = products)

@app.route("/product/<int:product_id>")
def product(product_id):
	product1=return_by_id(product_id)
	return render_template("product.html",product=product1)

@app.route("/cart")
def cart():
	cart_items=session.query(Cart).all()
	products=return_all()
	final_list=[]
	total=0
	for product in products:
		for cItem in cart_items:
			if cItem.productID==product.id:
				final_list.append(product)
				total+=product.price

	# shipping=0

	return render_template("cart.html",products=final_list,total=total)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
	#Add to cart
	add_to_cart_db(product_id)
	return redirect(url_for('home'))

@app.route("/delete_all_c")
def delete_all_cart():
	delete_all_cart_db() #Deletes everything from cart
	return redirect(url_for('cart'))

@app.route("/checkout")
def checkout():
	# subtotal = 
	# shipping = 
	# total_p_s = total 
	return render_template("checkout.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)