import csv
from database import PC, Laptop, Printer, engine
from sqlalchemy.orm import sessionmaker


def calculate_profitability_ratio(session, model):
    pc_query = session.query(PC).filter_by(model=model).first()
    laptop_query = session.query(Laptop).filter_by(model=model).first()

    if pc_query:
        pratio = pc_query.ram + pc_query.hd * pc_query.speed / pc_query.price
        print(f"Model {model} is a desktop computer (PC)")
    elif laptop_query:
        pratio = (
            (laptop_query.ram + laptop_query.hd)
            * laptop_query.speed
            / laptop_query.price
        )
        print(f"Model {model} is a laptop.")
    else:
        return None

    return pratio


def create_promo_sets(session):
    pc_printer_query = (
        session.query(PC, Printer).filter(PC.model == Printer.model).all()
    )
    laptop_printer_query = (
        session.query(Laptop, Printer).filter(Laptop.model == Printer.model).all()
    )

    with open("promo_sets.csv", mode="w", newline="") as file1:
        writer1 = csv.writer(file1)
        writer1.writerow(
            [
                "PC Model",
                "PC Price",
                "Printer Model",
                "Printer Type",
                "Printer Price",
                "PC + Printer promo price -10%",
            ]
        )
        for pc, printer in pc_printer_query:
            writer1.writerow(
                [
                    pc.model,
                    pc.price,
                    printer.model,
                    printer.type,
                    printer.price,
                    int((pc.price + printer.price) * 0.9),
                ]
            )
        writer1.writerow(
            [
                "Laptop Model",
                "Laptop Price",
                "Printer Model",
                "Printer Type",
                "Printer Price",
                "Laptop + Printer promo price -10%",
            ]
        )

        for laptop, printer in laptop_printer_query:
            writer1.writerow(
                [
                    laptop.model,
                    laptop.price,
                    printer.model,
                    printer.type,
                    printer.price,
                    int((laptop.price + printer.price) * 0.9),
                ]
            )

    print("The data was saved to CSV files.")


Session = sessionmaker(bind=engine)
session = Session()


# Task 1 : Check type of device by model

model = "P1"  # Select a model number to calculate profitability ratio
if profitability_ratio := calculate_profitability_ratio(session, model):
    print(f"Profitability ratio for model {model} is: {profitability_ratio}")


# Task 2 : Create 2 promosets; Laptop+Printer, PC+Printer with 10% discount and save it to csv file

create_promo_sets(session)
