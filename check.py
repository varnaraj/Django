# import os
# BASE_DIR2=os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR=os.path.join(BASE_DIR2+'/templates')
# print(BASE_DIR2);
# print(TEMPLATE_DIR)
from django.db import connection
con=connection.cursor