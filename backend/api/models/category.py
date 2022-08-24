class Category:
    __table__ = 'categories'
    columns = ['id', 'name']
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))


