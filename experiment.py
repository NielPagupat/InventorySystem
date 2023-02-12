import sqlite3
class Product:

    all = []

    def __init__(self, name, stock, trigger, trigger_value, oid, status):


        assert trigger > 0, f"stock {trigger} is less than 0"

        self.name = name
        self.stock = stock
        self.trigger = trigger
        self.trigger_value=trigger_value
        self.oid = oid
        self.status = status
        Product.all.append(self)


    @staticmethod
    def subtract(oid, sold):
        item = Product.all[oid-1]
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        item_ID = oid
        c.execute("SELECT * FROM inventory WHERE oid =" + str(item_ID))
        items = c.fetchall()

        originalval = item.stock
        soldval = int(sold)
        new_val = originalval - int(soldval)
        Bin_val = bin(new_val)
        updateid = oid

        c.execute("""UPDATE inventory SET
                                Product_Stock = :stock
                                WHERE oid = :oid""",
                  {

                      'stock': Bin_val,
                      'oid': updateid

                  })
        conn.commit()
        conn.close()

    @staticmethod
    def add(oid, resupply):
        item = Product.all[oid - 1]
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        item_ID = oid
        c.execute("SELECT * FROM inventory WHERE oid =" + str(item_ID))
        items = c.fetchall()

        originalval = item.stock
        addval = int(resupply)
        new_val = originalval + int(addval)
        new_triggerV = int((item.trigger/100)*new_val)
        Bin_newval = bin(new_val)
        Bin_triggerV = bin(new_triggerV)
        updateid = oid

        c.execute("""UPDATE inventory SET
                                        Product_Stock = :stock,
                                        Product_triggerV = :triggerV
                                        WHERE oid = :oid""",
                  {

                      'stock': Bin_newval,
                      'triggerV': Bin_triggerV,
                      'oid': updateid

                  })

        conn.commit()
        conn.close()

    @staticmethod
    def add_item(name, stock, Trigger):
        conn = sqlite3.connect("inventory.db")
        trigger_value = int((int(Trigger)/100)*stock)
        Bin_stock = bin(int(stock))
        Bin_trigger = bin(int(Trigger))
        Bin_triggerV = bin(int(trigger_value))
        c = conn.cursor()

        c.execute("INSERT INTO inventory VALUES (:p_name, :p_stock, :p_trigger, :p_triggerV)",
                  {
                      'p_name': name,
                      'p_stock': Bin_stock,
                      'p_trigger': Bin_trigger,
                      'p_triggerV' : Bin_triggerV
                  })

        conn.commit()
        conn.close()

    @staticmethod
    def edit_item(oid, new_name, new_stock, new_trigger):

        new_triggerV = (int(new_trigger)/100)*new_stock


        item = Product.all[oid-1]
        item.name = new_name
        item.stock = new_stock
        item.trigger = new_trigger
        item.triggerV = new_triggerV

        conn = sqlite3.connect("inventory.db")
        c = conn.cursor()

        item_ID = oid


        c.execute("""UPDATE inventory SET
                    Product_name = :name,
                    Product_stock = :stock,
                    Product_trigger = :trigger,
                    Product_triggerV = :triggerV
                    WHERE oid = :oid""",
                  {
                      'name': new_name,
                      'stock': bin(new_stock),
                      'trigger': bin(new_trigger),
                      'triggerV': bin(int(new_triggerV)),

                      'oid': item_ID

                  })

        conn.commit()
        conn.close()

    @staticmethod
    def delete_item(oid):
        Product.all.pop(int(oid)-1)
        conn = sqlite3.connect("inventory.db")
        c = conn.cursor()

        c.execute("DELETE from inventory WHERE oid = " + oid)
        Product.instantiate_from_csv()
        conn.commit()
        conn.close()

    @staticmethod
    def delete_all_item():
        Product.all.clear()

        conn = sqlite3.connect("inventory.db")
        c = conn.cursor()

        c.execute("DELETE from inventory")

        conn.commit()
        conn.close()

    def __repr__(self):
        return f"Product('{self.name}', {self.stock}, {self.trigger}, {self.trigger_value}, {self.oid}, {self.status})"

    @classmethod
    def instantiate_from_csv(cls):
        global stat
        Product.all.clear()
        conn = sqlite3.connect("inventory.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM inventory")
        items = c.fetchall()
        for item in items:
            item_stock = int(item[1], 2)
            item_trigger = int(item[2], 2)
            item_triggerV = int(item[3], 2)

            if int(item[1], 2) > item_triggerV:
                stat = 'good'
            elif int(item[1], 2) <= item_triggerV and int(item[1], 2)>0:
                stat = 'restock'
            elif int(item[1], 2) == 0:
                stat = 'sold out'

            Product(
                name=item[0],
                stock = item_stock,
                trigger= item_trigger,
                trigger_value= item_triggerV,
                oid= item[4],
                status= stat
            )
        conn.commit()
        conn.close()



'''
conn = sqlite3.connect("inventory.db")
c = conn.cursor()

c.execute( """CREATE TABLE inventory (
                    Product_name text,
                    Product_stock int,
                    Product_trigger int,
                    Product_triggerV int
                ) """ )



conn.commit()
conn.close()
'''

