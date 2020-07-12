import db_interface

#db_interface.add_user("510220220","California" ,"Irvine")

#db_interface.del_user("510220220")

db_interface.add_user("000000", "I should", "be here")
db_interface.add_user("000100", "I should", "be here")
db_interface.add_user("200000", "I should", "be here")
db_interface.add_user("000000", "I should", "be here")
print("Database: \n")
db_interface.print_subscribers()

db_interface.clear_subscribers()

print("Database: \n")
db_interface.print_subscribers()