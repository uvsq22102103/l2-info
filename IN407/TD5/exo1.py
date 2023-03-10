DBD = {69:("Kanga","Elie",19,False),
       96:("Dupuy","Raphael",19,True),
       12:("Aubert","Arnaud",25,True),
       1:("Legrand","Pierre",54,False)}

DBDIndex = {k: val[0] for k,val in DBD.items()}
print(DBDIndex)
DBDnumIP = {k: val for k,val in DBD.items() if k % 2}
print(DBDnumIP)
EnsIP = set(val for k,val in DBDIndex.items() if k % 2)
print(EnsIP)