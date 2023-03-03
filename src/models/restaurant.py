class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        #retirado o ".title()
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    #todos os métodos foram inseridos o "return" porque não estavam retornando nada
    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #alterado o nome cuisine_type para restaurant_nam
        #alterado o nome de restaurante que estava escrito errado
        return f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}.\nEsse restaurante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        #alterado o open de False para True/ number_served foi alterado de -2 para 0
        if not self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    #método para validar numero de consumidores
    def valid_customers_num(self, customers_num):
        if type(customers_num) is int and customers_num > 0:
            return True
        else:
            return False

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.valid_customers_num(total_customers):
            if self.open:
                self.number_served = total_customers
                return f"O número de consumidores agora é {self.number_served}."
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return "Total de consumidores inválido"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        #o método não estava incrementando foi adicionado "+="
        if self.valid_customers_num(more_customers):
            if self.open:
                self.number_served += more_customers
                return f"O número de consumidores agora é {self.number_served}."
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return "Tipo de consumidor inválido"
