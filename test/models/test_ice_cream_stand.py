import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    @pytest.fixture
    def restaurant_name(self):
        return 'Sorvete'

    @pytest.fixture
    def restaurant_type(self):
        return 'Sorveteria'

    @pytest.fixture
    def flavors_list(self):
        return ["chocolate","morango","baunilha"]

    @pytest.fixture
    def empty_list(self):
        return []

    def test_flavors_available(self,restaurant_name,restaurant_type,flavors_list,empty_list):
        #setup
        icecream = IceCreamStand(restaurant_name,restaurant_type,flavors_list)
        texto = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
        sabores = ""
        for flavor in flavors_list:
            sabores = sabores + "\n\t-" + flavor

        resultado_esperado = texto + "\n" + sabores

        #chamada
        resultado =icecream.flavors_available()

        #avaliação
        assert resultado == resultado_esperado
        assert icecream.flavors != empty_list

    def test_flavors_not_available(self,restaurant_name,restaurant_type,empty_list):
        #setup
        icecream = IceCreamStand(restaurant_name,restaurant_type,empty_list)

        resultado_esperado = "Estamos sem estoque atualmente!"

        #chamada
        resultado =icecream.flavors_available()

        #avaliação
        assert resultado == resultado_esperado
        assert icecream.flavors == empty_list

    def test_not_find_flavor(self,restaurant_name,restaurant_type,flavors_list):
        # setup
        icecream = IceCreamStand(restaurant_name, restaurant_type, flavors_list)
        find_flavor = "doce de leite"

        resultado_esperado = f"Não temos no momento {find_flavor}!"

        # chamada
        resultado = icecream.find_flavor(find_flavor)

        # avaliação
        assert resultado == resultado_esperado

    def test_find_flavor(self,restaurant_name,restaurant_type,flavors_list):
        # setup
        icecream = IceCreamStand(restaurant_name, restaurant_type, flavors_list)
        find_flavor = "baunilha"

        resultado_esperado = f"Temos no momento {find_flavor}!"

        # chamada
        resultado = icecream.find_flavor(find_flavor)

        # avaliação
        assert resultado == resultado_esperado

    def test_find_flavor_empty_list(self,restaurant_name,restaurant_type,empty_list):
        # setup
        icecream = IceCreamStand(restaurant_name, restaurant_type, empty_list)
        find_flavor = "leite"

        resultado_esperado = "Estamos sem estoque atualmente!"

        # chamada
        resultado = icecream.find_flavor(find_flavor)

        # avaliação
        assert resultado == resultado_esperado

    def test_add_flavor_already_in_list(self,restaurant_name,restaurant_type,flavors_list):
        # setup
        icecream = IceCreamStand(restaurant_name, restaurant_type, flavors_list)
        add_flavor = "morango"

        resultado_esperado = "\nSabor já disponivel!"

        # chamada
        resultado = icecream.add_flavor(add_flavor)

        # avaliação
        assert resultado == resultado_esperado

    def test_add_flavor_already_not_in_list(self,restaurant_name,restaurant_type,flavors_list):
        # setup
        icecream = IceCreamStand(restaurant_name, restaurant_type, flavors_list)
        add_flavor = "limão"
        # actual_list = icecream.flavors_available() + "\n\t-" + add_flavor
        actual_list = flavors_list.copy()
        actual_list.append(add_flavor)

        resultado_esperado = f"{add_flavor} adicionado ao estoque!"

        # chamada
        resultado = icecream.add_flavor(add_flavor)

        # avaliação
        assert resultado == resultado_esperado
        # assert actual_list == icecream.flavors_available()
        assert actual_list == icecream.flavors
