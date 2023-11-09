from database import PC, Printer, Product, Laptop, Session


session = Session()

products_data = [
    Product(maker="A", model="P1", type="PC"),
    Product(maker="B", model="P2", type="PC"),
    Product(maker="B", model="P3", type="Printer"),
    Product(maker="C", model="P4", type="Laptop"),
    Product(maker="D", model="P5", type="PC"),
    Product(maker="C", model="P6", type="Laptop"),
]
session.bulk_save_objects(products_data)
session.commit()

pcs_data = [
    PC(code=1, model="P1", speed=1000, ram=4096, hd=800, cd="8x", price=800),
    PC(code=2, model="P2", speed=1200, ram=8192, hd=1000, cd="12x", price=900),
    PC(code=3, model="P5", speed=1500, ram=2048, hd=500, cd="16x", price=1000),
]
session.bulk_save_objects(pcs_data)
session.commit()

laptops_data = [
    Laptop(code=4, model="P4", speed=2000, ram=16384, hd=256, screen=15, price=1400),
    Laptop(code=5, model="P6", speed=2000, ram=8192, hd=512, screen=13, price=1200),
]
session.bulk_save_objects(laptops_data)
session.commit()

printers_data = [
    Printer(code=6, model="P3", color="yes", type="Laser", price=300),
    Printer(code=7, model="P5", color="no", type="Matrix", price=200),
    Printer(code=8, model="P4", color="no", type="Laser", price=600),
]
session.bulk_save_objects(printers_data)
session.commit()

session.close()
