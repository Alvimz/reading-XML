class Person(object):

    def __init__(self) -> None:
        self._name = ""
        self._age = ""

class Father(Person):

    def __init__(self) -> None:
        super().__init__()
        self._number_of_childs = 0

