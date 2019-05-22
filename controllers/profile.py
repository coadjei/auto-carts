@auth.requires_login()
def save():
	profilerows = db(db.profile.created_by==session.auth.user.id).select(orderby=~db.profile.id)
	for x in profilerows:
		db.profile.shop_name.default = x.shop_name
		db.profile.shop_address.default = x.shop_address
		db.profile.shop_website.default = x.shop_website
		break;
	form = SQLFORM(db.profile).process()
	return locals()
