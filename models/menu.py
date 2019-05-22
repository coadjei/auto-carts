# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('products', 'view')),
    (T('Post'), False, URL('products', 'post')),
    (T('Profile'), False, URL('profile', 'save')),
]
