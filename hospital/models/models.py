class Pacient:
    def __init__(self, id_pacient, nom, cognom, simptomes):
        self.id_pacient = id_pacient
        self.nom = nom
        self.cognom = cognom
        self.simptomes = simptomes
        self.visites = []  # Lista de visitas a médicos

    def afegir_visita(self, visita):
        self.visites.append(visita)

    def __str__(self):
        return f"Pacient: {self.nom} {self.cognom}, Simptomes: {', '.join(self.simptomes)}"


class Metge:
    def __init__(self, id_metge, nom, cognom, num_colegiat):
        self.id_metge = id_metge
        self.nom = nom
        self.cognom = cognom
        self.num_colegiat = num_colegiat
        self.visites = []  # Lista de visitas a pacientes

    def atendre_pacient(self, pacient, diagnostic):
        visita = Visita(self, pacient, diagnostic)
        self.visites.append(visita)
        pacient.afegir_visita(visita)

    def __str__(self):
        return f"Metge: {self.nom} {self.cognom}, Colegiat: {self.num_colegiat}"


class Visita:
    def __init__(self, metge, pacient, diagnostic):
        self.metge = metge
        self.pacient = pacient
        self.diagnostic = diagnostic

    def __str__(self):
        return f"Visita: Pacient: {self.pacient.nom} {self.pacient.cognom} - Metge: {self.metge.nom} {self.metge.cognom}, Diagnòstic: {self.diagnostic}"


# Exemple d'ús

# Creem pacients
pacient1 = Pacient(1, "Joan", "Garcia", ["Febre", "Tos", "Mal de cap"])
pacient2 = Pacient(2, "Maria", "Lopez", ["Mal de panxa", "Nàusees"])

# Creem metges
metge1 = Metge(1, "Dr. Pere", "Martínez", "12345")
metge2 = Metge(2, "Dra. Anna", "Ribera", "67890")

# Creem visites i afegim els diagnòstics
metge1.atendre_pacient(pacient1, "Refredat comú")
metge2.atendre_pacient(pacient1, "Infecció respiratòria")
metge1.atendre_pacient(pacient2, "Gastritis")

# Mostrem els pacients, metges i visites
print(pacient1)
for visita in pacient1.visites:
    print(visita)

print(pacient2)
for visita in pacient2.visites:
    print(visita)

print(metge1)
for visita in metge1.visites:
    print(visita)

print(metge2)
for visita in metge2.visites:
    print(visita)
