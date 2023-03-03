from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            texto = "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            sabores = ""
            for flavor in self.flavors:
                sabores = sabores + "\n\t-" + flavor
            return texto + "\n" + sabores
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {flavor}!" #retorna uma lista e não o sabor passado
            else:
                return f"Não temos no momento {flavor}!" #retorna uma lista e não o sabor passado
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        #não é necessário validar se tem estoque
        if flavor in self.flavors:
            return "\nSabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"

