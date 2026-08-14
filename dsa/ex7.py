class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def adicionarConsulta(self, consulta):
        self.historico_consultas.append(consulta)

    def exibirConsultas(self):
        print(f"Consultas de {self.nome}:")
        for consulta in self.historico_consultas:
            print(f"- {consulta}")


paciente = Paciente("Maria", 30)
paciente.adicionarConsulta("10/08/2026 - Clinico geral")
paciente.adicionarConsulta("12/08/2026 - Dermatologista")
paciente.exibirConsultas()
