class Hotel:
    def listar(self):
        
        print ("")
    
class Quartos(Hotel):
    def reserva(self, nome, telefone, quarto):
        self.nome=nome
        self.telefone=telefone
        self.quarto=quarto
        

class Ap_luxo(Quartos):
    def listar_ap_luxo(self, ocupado=0):
        
        if ocupado == 1:
            print("Um quarto está reservado")
        elif ocupado == 2:
            print("Todos os quartos estão reservados")

class Ap_Master(Quartos):
    def listar_ap_master(self, ocupado=0):
        print("")

class Ap_Simples(Quartos):
    def listar_ap_simples(self, ocupado=0):
        print("")

class Ap_Simples_casal(Quartos):
    def listar_ap_simples_casal(self, ocupado=0):
        print("")

class Ap_Duplo(Quartos):
    def listar_ap_duplo(self, ocupado=0):
        print("")

class Ap_Duplo_casal(Quartos):
    def listar_ap_duplo_casal(self, ocupado=0):
        print("")
