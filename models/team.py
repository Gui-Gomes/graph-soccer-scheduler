class Team:
    # Constructor to initialize team attributes
    def __init__(self, acronym, name, city):
        self.__acronym = acronym
        self.__name = name
        self.__city = city

    # Property to get the acronym
    @property
    def acronym(self):
        return self.__acronym

    # Setter to set the acronym
    @acronym.setter
    def acronym(self, acronym):
        self.__acronym = acronym

    # Property to get the name
    @property
    def name(self):
        return self.__name

    # Setter to set the name
    @name.setter
    def name(self, name):
        self.__name = name

    # Property to get the city
    @property
    def city(self):
        return self.__city

    # Setter to set the city
    @city.setter
    def city(self, city):
        self.__city = city

    # Method to display team information
    def information(self):
        print(f"ACRONYM: {self.acronym}")
        print(f"NAME: {self.name}")
        print(f"CITY: {self.city}")
