#!/usr/bin/python3
'''Base class
'''
import json
class Base:
     '''Instances '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @classmethod
    def save_to_file(cls, list_objs):
        '''save file'''
        newl = []

        if list_objs:
            for y in list_objs:
                newl.append(cls.to_dictionary(y))
            with open(cls.__name__+'.json', mode="w") as f:
                f.write(Base.to_json_string(newl))

    @classmethod
    def create(cls, **dictionary):
        ''' create a new instance '''

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
            cls.update(dummy, **dictionary)
            return dummy

    @staticmethod
    def from_json_string(json_string):
        '''method json to string'''
        if json_string is None or len(json_string) is 0:
            return([])
        return json.loads(json_string)

   @staticmethod
   def to_json_string(list_dictionaries):
        '''method convert to json'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
             return("[]")
        else:
             return(json.dumps(list_dictionaries))
