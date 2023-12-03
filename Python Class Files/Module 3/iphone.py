#WAP to  store and display different versions , features and price of iPhones and define the functions to get the versions, cost , specs

class iPhone:
    def __init__(self, version, cost, specs):
        self.version = version
        self.cost = cost
        self.specs = specs

    def get_version(self):
        return self.version

    def get_cost(self):
        return self.cost

    def get_specs(self):
        return self.specs

# Create instances for different iPhone versions
iphone12 = iPhone("iPhone 12", "$699", {"Display": "6.1-inch"})
iphone12Pro = iPhone("iPhone 12 Pro", "$999", {"Display": "6.1-inch"})
iphone13 = iPhone("iPhone 13", "$799", {"Display": "6.1-inch"})
iphone13Pro = iPhone("iPhone 13 Pro", "$999", {"Display": "6.1-inch"})

# Print details
print(f"{iphone12.get_version()} costs {iphone12.get_cost()} and has these features: {iphone12.get_specs()}")
print(f"{iphone12Pro.get_version()} costs {iphone12Pro.get_cost()} and has these features: {iphone12Pro.get_specs()}")
print(f"{iphone13.get_version()} costs {iphone13.get_cost()} and has these features: {iphone13.get_specs()}")
print(f"{iphone13Pro.get_version()} costs {iphone13Pro.get_cost()} and has these features: {iphone13Pro.get_specs()}")
