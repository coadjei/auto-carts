# -*- coding: utf-8 -*-

db = DAL("sqlite://storage.sqlite")
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
auth = Auth(db) 
auth.define_tables(username=True)

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
db.define_table('products',
                Field('product_name', requires=IS_NOT_EMPTY()),
                Field('product_price', requires=IS_NOT_EMPTY()),
                Field('product_image', 'upload'),
                Field('product_status', requires=IS_IN_SET(['active','inactive'])),
                Field('shop_name', requires=IS_NOT_EMPTY()),
                Field('shop_address', requires=IS_NOT_EMPTY()),
                Field('shop_website', requires=IS_URL()),
                auth.signature
                )


db.define_table('profile',
                Field('shop_name'),
                Field('shop_address'),
                Field('shop_website'),
                auth.signature
                )

db.define_table('internet_orders',
                Field('productId', type='integer'),
                Field('qty', type='integer'),
                Field('userId', type='integer'),
                Field('status'),
                Field('date_ordered')
                )
