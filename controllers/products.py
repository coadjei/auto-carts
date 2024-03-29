

def proc():
	prodDict = {}
	productRows = db(db.products).select()
	for x in productRows:
		prodDict [x.id] = x.product_name
	date_ordered = str(request.now.year) + "-" + str(request.now.month) + "-" + str(request.now.day)
	qty = request.vars.qty
	productId = request.vars.productId
	userId = session.auth.user.id
	sql = "Insert into internet_orders (productId,userId,qty,status,date_ordered) values "
	sql = sql + "(" + str(productId) + "," + str(userId) + "," + str(qty) + ",'cart'," + str(date_ordered) +"')"
	r = db.executesql (sql)
	rows = db (db.internet_orders.userId==session.auth.user.id).select(orderby=~db.internet_orders.id)
	return locals()

@auth.requires_login()
def post():
	profilerows = db(db.profile.created_by==session.auth.user.id).select(orderby=~db.profile.id)
	for x in profilerows:
		db.products.shop_name.default = x.shop_name
		db.products.shop_address.default = x.shop_address
		db.products.shop_website.default = x.shop_website
		break;
	form = SQLFORM(db.products).process()
	return locals()


def view():
	userdict = {}
	userrows = db(db.auth_user).select()
	for x in userrows:
		userdict[x.id] = x.first_name + " " + x.last_name
	rows = db(db.products.product_status=='active').select(orderby=~db.products.id)
	return locals()

@auth.requires_login()
def myposts():
	rows = db(db.products.created_by==session.auth.user.id).select(orderby=db.products.product_status | ~db.products.id)
	return locals()

@auth.requires_login()
def update():
	isValid = False
	row = db(db.products.id==request.args(0)).select()
	for x in row:
		if x.created_by==session.auth.user.id:
			 isValid = True
	if isValid:
		record = db.products(request.args(0)) or redirect(URL('view'))
		form = SQLFORM(db.products, record)
		if form.process().accepted:
			 response.flash = T('Record Updated')
		else:
			response.flash = T('Please complete the form.')
	return locals()

def index(): return dict(message="hello from products.py")