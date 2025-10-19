from lei import Restaurant

restaurant=Restaurant('coco','tai','2')
restaurant.open_restaurant()

from lei2 import Admin

a=Admin('nick','yang')
a.privileges.show_privileges()
a.print_name()

admin=Admin('nick','jack')
admin.privileges.show_privileges()
admin.print_name()