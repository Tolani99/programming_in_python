import importlib
import filechanges

# importlib.reload(sample)
# importlib.reload(sample)

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass
for i in range(5):
    changes()
    input("Hit enter to reload ...")