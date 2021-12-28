    #this file is not used
import itertools
class Person:
    ID = itertools.count()
    def __init__(self, name, parent=None, level=0):
        self.id = self.__class__.ID.next() # next(self.__class__.ID) in python 2.6+
        self.parent = parent
        self.name = name
        self.level = level
        self.children = []

def createTree(d, parent=None, level=0):
    if d:
        member = Person(d['parent'], parent, level)
        level = level + 1
        member.children = [createTree(child, member, level) for child in d['children']]
        return member

        # my_tree is the name of your dictionary
