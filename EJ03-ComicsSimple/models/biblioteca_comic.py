from datetime import date

# 1. Definición del modelo de còmic
class Comic:
    def __init__(self, id_comic, titulo, autor, anio_publicacion):
        self.id_comic = id_comic
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return f"{self.titulo} de {self.autor} ({self.anio_publicacion})"


# 2. Definición del modelo de soci (socio)
class Soci:
    def __init__(self, id_soci, nom, cognom):
        self.id_soci = id_soci
        self.nom = nom
        self.cognom = cognom

    def __str__(self):
        return f"{self.nom} {self.cognom} (ID: {self.id_soci})"


# 3. Definición del modelo d'exemplar de préstec (ejemplar de préstamo)
class ExemplarPrestec:
    def __init__(self, comic, soci=None, data_inici=None, data_final=None):
        self.comic = comic
        self.soci = soci
        self.data_inici = data_inici
        self.data_final = data_final

    def prestar(self, soci, data_inici, data_final):
        # Validación de fechas
        if data_inici > date.today():
            raise ValueError("La data de préstec no pot ser posterior al dia d'avui.")
        if data_final < date.today():
            raise ValueError("La data prevista de tornada no pot ser anterior al dia d'avui.")

        self.soci = soci
        self.data_inici = data_inici
        self.data_final = data_final

    def __str__(self):
        return f"Còmic: {self.comic.titulo}, Prestado a: {self.soci.nom} {self.soci.cognom}, Desde: {self.data_inici} Hasta: {self.data_final}"


# Ejemplo de uso

# Crear cómics
comic1 = Comic(1, "Spider-Man", "Stan Lee", 1962)
comic2 = Comic(2, "Batman", "Bob Kane", 1939)

# Crear socios
soci1 = Soci(1, "Joan", "Garcia")
soci2 = Soci(2, "Maria", "Lopez")

# Crear ejemplares de préstamo
exemplar1 = ExemplarPrestec(comic1)
exemplar2 = ExemplarPrestec(comic2)

# Prestar cómics (validando fechas)
try:
    exemplar1.prestar(soci1, date(2024, 12, 17), date(2025, 1, 17))
    exemplar2.prestar(soci2, date(2024, 12, 17), date(2025, 1, 17))
    
    # Mostrar la información de los ejemplares prestados
    print(exemplar1)
    print(exemplar2)
except ValueError as e:
    print(e)

