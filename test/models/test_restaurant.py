import pytest

from src.models.restaurant import Restaurant

class TestRestaurant:

    @pytest.fixture
    def restaurant_name(self):
        return 'Sushi da Hora'

    @pytest.fixture
    def restaurant_type(self):
        return 'Japonesa'

    def test_describe_restaurant(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        resultado_esperado = f"Esse restaurante se chama {restaurant_name} e serve {restaurant_type}.\nEsse restaurante está servindo {restaurante.number_served} consumidores desde que está aberto."

        #chamada
        resultado = restaurante.describe_restaurant()

        #avaliação
        assert resultado == resultado_esperado

    def test_open_restaurant(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        resultado_esperado = f"{restaurant_name} agora está aberto!"

        #chamada
        resultado = restaurante.open_restaurant()

        #avaliação
        assert resultado == resultado_esperado
        assert restaurante.open == True
        assert restaurante.number_served == 0

    def test_already_open_restaurant(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        resultado_esperado = f"{restaurant_name} já está aberto!"
        restaurante.open_restaurant()

        #chamada
        resultado = restaurante.open_restaurant()

        #avaliação
        assert resultado == resultado_esperado
        assert restaurante.open == True
        assert restaurante.number_served == 0

    def test_close_restaurant(self, restaurant_name, restaurant_type):
        # setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        restaurante.open_restaurant()
        resultado_esperado = f"{restaurant_name} agora está fechado!"

        # chamada
        resultado = restaurante.close_restaurant()

        # avaliação
        assert resultado == resultado_esperado
        assert restaurante.open == False
        assert restaurante.number_served == 0

    def test_already_close_restaurant(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        resultado_esperado = f"{restaurant_name} já está fechado!"

        #chamada
        resultado = restaurante.close_restaurant()

        #avaliação
        assert resultado == resultado_esperado
        assert restaurante.open == False
        assert restaurante.number_served == 0

    def test_set_number_served_success(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        restaurante.open_restaurant()
        customers = 15
        resultado_esperado = f"O número de consumidores agora é {customers}."

        #chamada
        resultado = restaurante.set_number_served(customers)

        #avaliação
        assert resultado == resultado_esperado
        assert restaurante.number_served == customers

    def test_set_number_served_closed(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        customers = 15
        resultado_esperado = f"{restaurant_name} está fechado!"

        #chamada
        resultado = restaurante.set_number_served(customers)

        #avaliação
        assert resultado == resultado_esperado
        assert restaurante.number_served == 0

    def test_set_number_served_invalid(self, restaurant_name, restaurant_type):
        #setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        customers = "15"
        resultado_esperado = "Total de consumidores inválido"

        #chamada
        resultado = restaurante.set_number_served(customers)

        #avaliação
        assert resultado == resultado_esperado
        assert restaurante.number_served == 0

    def test_increment_number_served(self, restaurant_name, restaurant_type):
        # setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        increment = 1
        restaurante.open_restaurant()
        restaurante.set_number_served(10)
        total = increment + restaurante.number_served
        resultado_esperado = f"O número de consumidores agora é {total}."

        # chamada
        resultado = restaurante.increment_number_served(increment)

        # avaliação
        assert resultado == resultado_esperado
        assert restaurante.number_served == total

    def test_increment_number_served_closed(self, restaurant_name, restaurant_type):
        # setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        increment = 1
        restaurante.set_number_served(10)
        total = increment + restaurante.number_served
        resultado_esperado = f"{restaurant_name} está fechado!"

        # chamada
        resultado = restaurante.increment_number_served(increment)

        # avaliação
        assert resultado == resultado_esperado
        assert restaurante.number_served == 0

    def test_increment_number_served_invalid(self, restaurant_name, restaurant_type):
        # setup
        restaurante = Restaurant(restaurant_name, restaurant_type)
        increment = "1"
        restaurante.open_restaurant()
        resultado_esperado = "Tipo de consumidor inválido"

        # chamada
        resultado = restaurante.increment_number_served(increment)

        # avaliação
        assert resultado == resultado_esperado

