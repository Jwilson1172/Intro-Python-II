# Define a Store using OOP principles 

from product import Equipment, Clothing

class Store:
    def __init__(self, name, departments):
        self.name = name
        # departments will be a dict of Department instances 
        self.departments = departments
        # self.departments = self.init_departments(departments)

    def __str__(self):
        # this will print out the name of the Store 
        # as well as any departments that the Store has 
        output = f"{self.name}\n"
        for id in self.departments:
            output += "  id: " + str(id) + ", name: " + self.departments[id].get_name() + "\n" 
        return output

    # Take in a string of department names and returns a list of Department instances 
    # def init_departments(self, departments):
        # instances = {}
        # for key, val in departments.items():
        #     instances[key] = Department(key, val)
        # return instances
        # return [Department(i + 1, d) for i, d in enumerate(departments)]
        # return {key: Department(key, val) for key, val in departments.items()}

class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products
    
    def __str__(self):
        return f"Department {self.id}: {self.name}"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def print_products(self):
        for p in self.products:
            print(p)

# Let's go ahead and add a different ID to each department 
# To do this, we could change the departments list to a dict 
# so that we can have the ID as key and name as value 
# Or, we could have the departments list store tuples, where each 
# tuple has the name and ID 

# Why tuples vs dicts for this representation 
# departments = [
#     ("Running", 101),
#     ("Fishing", 103),
#     ("Baseball", 45), 
#     ("Basketball", 87)
# ]
# We can now easily look up a department by its ID 
# departments[103] => "Fishing"
# So we get efficient lookup for our departments 
departments = {
    101: Department(101, "Running", [Clothing("Running Shorts", 15, "Cotton", "Black")]),
    103: Department(103, "Fishing", [Equipment("Rod", 200, 1, "Fishing")]),
    45: Department(45, "Baseball", [Equipment("Bat", 50, 2, "Baseball")]),
    87: Department(87, "Basketball", [Equipment("Bat", 50, 2, "Baseball")]),
}

my_store = Store("The Dugout", departments)

# add a way for a user to select departments
print(my_store)
selection = int(input("Select a department number: "))

# Change this so that we're accessing Departments from the "canonical" list
# of Departments 
print(f"You selected Department {selection}, {my_store.departments[selection].get_name()}")
print("Products in this Department: ")
my_store.departments[selection].print_products()

# There's no easy way to access some department "outside" of our Store class 

# Let's add a more streamlined way to add Departments to our Store 
# Let's add a methon on the Department class that will take in a list of Strings
# representing Department names, and create the Department instances for us.
