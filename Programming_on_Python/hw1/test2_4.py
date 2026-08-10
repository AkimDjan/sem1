dct=dict()
dct['First']=234
dct['Second']=345
dct['Third']=456
key=dct['First']
del dct['First']
dct['First']=key
#del dct[tuple(dct.keys())[0]]

print(tuple(dct.keys()))