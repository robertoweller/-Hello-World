class Test():
    def __init__(self):
        self.cagado = 50
        self.sla()

    def sla(self):
        print(self.cagado)

# quando eu chamo essa classe
# note que a a sla esta sendo linkada pela função __inti__
# Sendo obrigado sempre usar o self dentro dos parentes 
# sendo obrigado usar antes das variaveis também
Test()
