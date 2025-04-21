class Country:
    """
    A class to represent a country and its happiness-related factors.
    Stores values for environment, economy, culture, healthcare, and education.
    Uses encapsulation with private fields and getter/setter methods.
    """

    def __init__(self, name, environment, economy, culture, healthcare, education):
        # Initialize private attributes using setters
        self.set_name(name)
        self.set_environment(environment)
        self.set_economy(economy)
        self.set_culture(culture)
        self.set_healthcare(healthcare)
        self.set_education(education)

    # Setters
    def set_name(self, name): self.__name = name
    def set_environment(self, environment): self.__environment = environment
    def set_economy(self, economy): self.__economy = economy
    def set_culture(self, culture): self.__culture = culture
    def set_healthcare(self, healthcare): self.__healthcare = healthcare
    def set_education(self, education): self.__education = education

    # Getters
    def get_name(self): return self.__name
    def get_environment(self): return self.__environment
    def get_economy(self): return self.__economy
    def get_culture(self): return self.__culture
    def get_healthcare(self): return self.__healthcare
    def get_education(self): return self.__education

    def calculate_happiness(self):
        """
        Calculates the average of all five factors and returns it
        rounded to 2 decimal places.
        """
        total = (self.get_environment() + self.get_economy() +
                 self.get_culture() + self.get_healthcare() +
                 self.get_education())
        return round(total / 5, 2)


class HappinessMeter:
    """
    A class to manage multiple Country objects and measure their happiness.
    """

    def __init__(self):
        # List to store all countries added
        self.countries = []

    def add_country(self, country):
        """
        Adds a Country object to the list of countries.
        """
        self.countries.append(country)

    def measure_happiness(self):
        """
        Iterates over all countries and prints their happiness index.
        """
        print("\nHappiness Measurement:")
        for country in self.countries:
            # Print country name and its happiness index
            print(f"{country.get_name()} : {country.calculate_happiness()}")


def main():
    """
    The main function that runs the program.
    Handles user input and interaction with the HappinessMeter.
    """
    meter = HappinessMeter()  # Create an instance of HappinessMeter

    # Ask user how many countries they want to enter
    count = int(input("Enter the number of countries: "))

    # Loop through based on how many countries user wants to input
    for i in range(count):
        print(f"\nEnter details for country {i + 1}:")

        # Take input for all factors of the country
        name = input("Enter the name of country: ")
        environment = int(input("Enter environment factor (0-100): "))
        economy = int(input("Enter economy factor (0-100): "))
        culture = int(input("Enter culture factor (0-100): "))
        healthcare = int(input("Enter healthcare factor (0-100): "))
        education = int(input("Enter education factor (0-100): "))

        # Create a Country object using the inputs (setters will assign values)
        country = Country(name, environment, economy, culture, healthcare, education)

        # Add the country to the meter
        meter.add_country(country)

    # Measure and display happiness for each country
    meter.measure_happiness()


# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()
