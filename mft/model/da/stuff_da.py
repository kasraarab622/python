from mft.model.da.database import DatabaseManager
from mft.model.entity.stuff import Stuff
from sqlalchemy import between
class StuffDa(DatabaseManager):
        def find_by_name(self, name):
            self.make_engine()
            result = self.session.query(Stuff).filter(Stuff.name == name)
            self.session.close()
            return result
         def find_by_brand(self, brand):
             self.make_engine()
             result = self.session.query(Stuff).filter(Stuff.brand == brand)
             self.session.close()
             return result


         def find_by_description(self, description):
            self.make_engine()
            result = self.session.query(Stuff).filter(Stuff.description.like(description))
            self.session.close()
            return result


        def find_by_price_range(self, start_price, end_price):
                self.make_engine()
                result = self.session.query(Stuff).filter(between(Stuff.price,start_price,end_price))
                self.session.close()
                return result
         def find_by_rent_price_range(self, start_price, end_price):
             self.make_engine()
             result = self.session.query(Stuff).filter(between(Stuff.price, start_price, end_price))
             self.session.close()
             return result

         def find_by_condition(self, rent_condition):
             self.make_engine()
             result = self.session.query(Stuff).filter(Stuff.rent_condition.like(rent_condition))
             self.session.close()
             return result

    # stuff= Stuff(1,"Mobile","Samsung","de", 1000, "adada","adasdasda",200)
    # print(stuff)
    #
    # da = StuffDa()
    # # da.save(stuff)
# print(da.find_all())