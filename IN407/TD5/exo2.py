TAILLE_LOT = 8
STOCK = {"Hammer": 56,
         "Screwdriver": 183,
         "Wrench": 71,
         "Pliers": 12,
         "Boite": 5}



nombre_lots = lambda nombre_objets,taille_lot: nombre_objets//taille_lot
commande = ["Hammer","Wrench","Fleurs"]

commande_response = {}
for obj in commande:
    if nombre_lots(STOCK.get(obj,0),TAILLE_LOT):
        commande_response[obj] = nombre_lots(STOCK.get(obj,0),TAILLE_LOT)
commande_response = {obj: nombre_lots(STOCK.get(obj,0),TAILLE_LOT) for obj in commande if nombre_lots(STOCK.get(obj,0),TAILLE_LOT)}
commande_response = {obj: lots for obj in commande if (lots := nombre_lots(STOCK.get(obj,0),TAILLE_LOT))}
commande_response = ((obj,lots) for obj in commande if (lots := nombre_lots(STOCK.get(obj,0),TAILLE_LOT)))
for obj, lots in commande_response:
    print(obj, lots)
# Ci dessus usage du Walrus (:=) il s'agit d'une variable temporaire servant à ne pas executer deux fois le resultat d'une opération/fonction