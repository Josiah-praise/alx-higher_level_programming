#!/usr/bin/python3
'''Base class'''


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        dumps = __import__('json').dumps
        return dumps(list_dictionaries) if list_dictionaries\
            is not None else dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            list_objs_json_repr = Base.to_json_string(list_objs)

        file_name = cls.__name__ + '.json'

        with open(file_name, mode='w', encoding='utf-8') as stream:
            if list_objs is not None:
                stream.write(list_objs_json_repr)
            else:
                stream.write('[]')

    @classmethod
    def from_json_string(cls, json_string):
        '''
        returns the list of the JSON string
        representation json_string
        '''
        loads = __import__('json').loads

        return [] if json_string is None or\
            len(json_string) == 0 else loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        obj = cls(2, 3) if cls.__name__ == 'Rectangle' else cls(2)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        file = cls.__name__ + '.json'
        try:
            with open(file, mode='r', encoding='utf-8') as stream:
                file_content = stream.read()
        except FileNotFoundError:
            return []

        list_of_dict = cls.from_json_string(file_content)
        return [cls.create(**dict_) for dict_ in list_of_dict]
