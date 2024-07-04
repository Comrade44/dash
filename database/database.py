from sqlalchemy import create_engine, update, insert, select, MetaData, Table, Column, Integer, String

class Database:
    def __init__(self):
        self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        self.metadata_obj = MetaData()
        self.item_table = Table(
            "item",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("content", String),
            Column("list_number", Integer)
        )
        self.metadata_obj.create_all(self.engine)

    def add_item(self, content, list_number):
        stmt = insert(self.item_table).values(content=content, list_number=list_number)
        with self.engine.begin() as conn:
            conn.execute(stmt)

    def select_items(self, list_number):
        stmt = select(self.item_table.c.content).where(self.item_table.c.list_number == list_number)
        with self.engine.begin() as conn:
            result = conn.execute(stmt)
        results = [row.content for row in result]
        return results

    def delete_items(self, item_id):
        stmt = update(self.item_table).where(self.item_table.c.id == item_id)
        with self.engine.begin() as conn:
            conn.execute(stmt)

    def update_item_content(self, item_id, content):
        stmt = update(self.item_table).where(self.item_table.c.id == item_id).values(content=content)
        with self.engine.begin() as conn:
            conn.execute(stmt)