import logging
logging.basicConfig(level=logging.DEBUG)

class Person:
    def __init__(self, name, age):
        logging.debug("Entering person constructor")
        if not self.__validateName__(name):
            logging.error("Name provided in Person construct is invalid")
            raise ValueError("Name is invalid")
        self._name = name
        if not self.__validateAge__(age):
            logging.error("Age provided in Person construct is invalid")
            raise ValueError("Age is invalid")
        self._age = age
        logging.debug("Exiting person constructor")

    @property
    def age(self):
        """ The docstring for the age property """
        logging.debug("Entering age")
        return self._age
        logging.debug("Exiting age")

    @age.setter
    def age(self, value):
        logging.debug("Entering set_age")
        if not self.__validateAge__(value):
            logging.error("Age provided is invalid!")
            raise ValueError("Age is invalided!")
        self._age = value
        logging.debug("Exiting set_age")

    @age.deleter
    def age(self):
        logging.debug("Entering del_age")
        del self._age
        logging.debug("Exiting del_age")

    @property
    def name(self):
        logging.debug("Entering name")
        return self._name
        logging.debug("Exiting name")

    @name.setter
    def name(self, value):
        logging.debug("Entering set_name")
        if not self.__validateName__(value):
             raise ValueError("Name is invalid")
        self._name = value
        logging.debug("Exiting set_name")

    @name.deleter
    def name(self):
        logging.debug("Entering del_name")
        del self._name
        logging.debug("Exiting del_name")

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)

    def __validateName__(self, name):
         logging.debug("Entering __validateName__")
         logging.debug("Exiting __validateName__")
         return bool(name) and isinstance(name, str) # an empty or None string resolves as false

    def __validateAge__(self, age):
         logging.debug("Entering __validateAge__")
         logging.debug("Exiting __validateAge__")
         return age and isinstance(age, int) and age > 0

if __name__ == "__main__":
    person = Person('John', 54)
    logging.info(person)
    logging.info(person.age)
    logging.info(person.name)
    person.age = 21
    logging.info(person)
