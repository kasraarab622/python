from mft.model.da.stuff_da import StuffDa
from mft.model.entity.stuff import Stuff

class StuffController:
    @classmethod
    def save(cls,name,brand,description,price,image,rent_condition,rent_price):
        try:
            stuff = Stuff()
            stuff.name=name
            stuff.brand=brand
            stuff.description=description
            stuff.price=price
            stuff.image=image
            stuff.rent_condition=rent_condition
            stuff.rent_price=rent_price
            da =StuffDa()
            da.save(Stuff)
            return True,Stuff
        except Exception as (e):
            return e

    @classmethod
    def edit(cls,code, name, brand, description, price, image, rent_condition, rent_price):
        try:
            da =StuffDa()
            Stuff=da.find_by_id(code)
            Stuff.name = name
            Stuff.brand=brand
            Stuff.description=description
            Stuff.price=price
            Stuff.image =image
            Stuff.rent_condition=rent_condition
            Stuff.rent_price=rent_price
            da.edit(Stuff)
            return True,Stuff
        except Exception as (e):
            return e

    @classmethod
    def remove(self, code):
        try:
            da = StuffDa()
            Stuff =da.find_by_id(code)
            da.remove(Stuff)
            return code
        except Exception as (e):
            return e

    @classmethod
    def find_all(self):
        try:
            da =StuffDa()
            return da.find_all(Stuff)
        except Exception as (e):
            return e

    @classmethod
    def find_by_code(self,code):
        try:
            da =StuffDa()
            return da.find_by_id(Stuff,id)
        except Exception as (e):
            return e

    @classmethod
    def find_by_name(self,name):
        try:
            da=StuffDa()
            return da.find_by_name(Stuff,name)
        except Exception as (e):
            return e

    def find_by_brand(self,brand):
        try:
            da=StuffDa()
            return da.find_by_brand(brand)
        except Exception as (e):
            return e

    def  find_by_description(self,description):
        try:
            da =StuffDa()
            return da.find_by_description(Stuff,description)
        except Exception as (e):
            return e

    def find_by_price(self,start_price,end_price):
        try:
            da =StuffDa()
            return da.find_by_price_range(Stuff,start_price,end_price)
        except Exception as (e):
            return e

    def find_by_rent_price(self,start_price,end_price):
        try:
            da =StuffDa()
            return da.find_by_rent_price_range(Stuff,start_price,end_price)
        except Exception as (e):
            return e

    def find_by_condition(self,rent_condition):
        try:
            da =StuffDa()
            return da.find_by_condition(Stuff,rent_condition)
        except Exception as (e):
            return e