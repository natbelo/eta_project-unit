from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand

#restaurante = Restaurant("Sushi da Hora","Japonesa")
#
# # print(restaurante.describe_restaurant())
#
# print(restaurante.open_restaurant())
# print(restaurante.open_restaurant())
# # print(restaurante.close_restaurant())
# # # print(restaurante.close_restaurant())
# # print(restaurante.set_number_served(10))
# # # print(restaurante.describe_restaurant())
# # print(restaurante.increment_number_served(1))
# # # print(restaurante.describe_restaurant())
#
# print(restaurante.valid_costumers_num(10))

flavors_list = ["chocolate","morango","baunilha"]
iceCream = IceCreamStand("Sorvete", "Soverteria", flavors_list)
actual_list = flavors_list.copy()
actual_list.append("manga")
print(actual_list)
print(flavors_list)

# iceCream = IceCreamStand("Sorvete", "Soverteria", [])

# print(iceCream.flavors_available())
# # print(iceCream.find_flavor("teste"))
# print(iceCream.add_flavor("teste"))
# print(iceCream.add_flavor("chocolate"))
# print(iceCream.add_flavor("teste"))
# print(iceCream.flavors_available())
