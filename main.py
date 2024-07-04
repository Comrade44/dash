from database.database import Database

item_db = Database()

print(item_db.add_item("Test note 1", 1))
item_db.add_item("Test note 2", 1)
item_db.add_item("Test note 3", 2)
item_db.add_item("Test note 4", 2)
item_db.update_item_content(2, "Test note updated")
print(item_db.select_items(2))
print(item_db.select_items(1))
