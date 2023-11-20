import re
from mft.model.entity.base import Base
from sqlalchemy import Column,Integer,String,Boolean


class Stuff(Base):
    __tablename__ = "stuff_tbl"

    code = Column(Integer, primary_key=True)
    name = Column(String(20))
    brand = Column(String(20))
    description = Column(String(200))
    price = Column(Integer)
    image = Column(String(45))
    rent_condition = Column(String(200))
    rent_price = Column(Integer)
    deleted = Column(Boolean)

    def __init__(self, code, name, brand, description, price, image, rent_condition, rent_price,deleted=0):
        self.code = code
        self.name = name
        self.brand = brand
        self.description = description
        self.price = price
        self.image = image
        self.rent_condition = rent_condition
        self.rent_price = rent_price
        self.deleted = deleted

    def __repr__(self):
        return str(self.__dict__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name,str) and re.match("[a-zA-Z]{2,20}$",name):
            self._name
        else:
            raise ValueError("Invalid Name")

    # props
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand,str) and re.match("^[a-zA-Z\s]{2,20}$", brand):
            self._brand = brand
        else:
            raise ValueError("Invalid Brand")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description,str) and re.match("^[a-zA-Z\d]{10,200}$",description):
            self._description
        else:
            raise ValueError("Invalid Description")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price,int) and price >0:
            self._price
        else:
            raise ValueError("Invalid Price")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image

    @property
    def rent_condition(self):
        return self._rent_condition

    @rent_condition.setter
    def rent_condition(self, rent_condition):
        if isinstance(rent_condition,str) and re.match("^[a-zA-z\d]{200}$",rent_condition):
            self._rent_condition
        else:
            raise ValueError("Invalid RentCondition")

    @property
    def rent_price(self):
        return self._rent_price

    @rent_price.setter
    def rent_price(self, rent_price):
        if isinstance(rent_price,int) and rent_price>0:
          self._rent_price
        else:
            raise ValueError("Invalid RentPrice")