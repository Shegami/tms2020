"""
Логика работы с БД.
"""

from cars.classes import Brand, Car, session


#  add brand to DB
def add_brand(name):
    brand = Brand(name=name)
    session.add(brand)
    session.commit()


#  add car to DB
def add_car(**kwargs):
    car = Car(**kwargs)
    session.add(car)
    session.commit()


#  get brand
def get_brand(brand_id=None, name=None):
    if brand_id is not None:
        brand = session.query(Brand).get(brand_id)
        return brand
    elif name is not None:
        brand = session.query(Brand).filter(
            Brand.name == name
        ).first()
        return brand
    else:
        brands = session.query(Brand).all()
        return brands


#  get cars
def get_car(car_id=None):
    if car_id is None:
        cars = session.query(Car).all()
        return cars
    else:
        car = session.query(Car).get(car_id)
        return car


#  update brand in DB by ID
def update_brand(brand_id, name):
    brand = session.query(Brand).get(brand_id)
    if brand:
        brand.name = name
        session.commit()


#  update car in DB by ID
def update_car(**kwargs):
    car = session.query(Car).get(kwargs['car_id'])
    car.model = kwargs['model']
    car.release_year = kwargs['release_year']
    car.brand = kwargs['brand']
    session.commit()


#  delete brand from DB by ID
def delete_brand(brand_id):
    brand = session.query(Brand).get(brand_id)
    session.delete(brand)
    session.commit()


# delete car from DB by ID
def delete_car(car_id):
    car = session.query(Car).get(car_id)
    session.delete(car)
    session.commit()
