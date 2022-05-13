class Products():
    COLLECTION_NAME = 'products'

def __init__(self,context):
    self.context = context

@classmethod
def Create():
    pass

@classmethod
def Read():
    try:
        product = db.Products.find()
        print ('\n All data from Products Database \n')
    except Exception as ex:
        print(ex)

@classmethod
def Update():
    pass

@classmethod
def Delete():
    pass
