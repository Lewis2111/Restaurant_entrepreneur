from meal_factory import Meal_Factory

class Meal_Factory:
    def create_meal(self, type):
        if type == 'Pizza':
            return Pizza()
        elif type == 'Salad':
            return Salad()
        
        
        
Factory = Meal_Factory()   

Meal_one = Meal_Factory('pizza')

print(Meal_one.type)

Meal_two = Meal_Factory('Salad')

print(Meal_two.type)

Meal_three = Meal_Factory('Pasta')

print(Meal_three.type)
        