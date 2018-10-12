
def calculerSalaire(metier, annees):
    if metier == "architecte" and annees == 4:
        return 4000
    if metier == "medecin" and annees == 8:
        return 7000
    if metier == "consultant" and annees == 5:
        return 5000

print("Le salaire d'un architecte après 4 années d'expérience est de " + str(calculerSalaire("architecte", 4)))
print("Le salaire d'un médecin après 8 années d'expérience est de " + str(calculerSalaire("medecin", 8)))
print("Le salaire d'un consultant après 5 années d'expérience est de " + str(calculerSalaire("consultant", 5)))
