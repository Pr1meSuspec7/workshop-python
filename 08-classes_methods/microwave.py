#################### Class ####################


class Microwave:
    def __init__(self, brand, power_rating) -> None:
        self.brand = brand
        self.power_rating = power_rating

smeg = Microwave('Smeg', 'B')
print(smeg)
print(smeg.brand)
print(smeg.power_rating)

bosh = Microwave('bosh', 'C')
print(bosh)
print(bosh.brand)
print(bosh.power_rating)


#################### Method ####################


class Microwave:
    def __init__(self, brand, power_rating) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave {self.brand} is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave {self.brand} is now turned off.')
        else:
            print(f'Microwave {self.brand} is already turned off.')

    def run(self, seconds) -> None:
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds.')
        else:
            print('Turn on your microwave first...')

smeg = Microwave('Smeg', 'B')
bosh = Microwave('bosh', 'C')


#################### Dunder Method ####################


class Microwave:
    def __init__(self, brand, power_rating) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave {self.brand} is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is now turned on.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave {self.brand} is now turned off.')
        else:
            print(f'Microwave {self.brand} is already turned off.')

    def run(self, seconds) -> None:
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds.')
        else:
            print('Turn on your microwave first...')

    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'
    
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'

smeg = Microwave('Smeg', 'B')
