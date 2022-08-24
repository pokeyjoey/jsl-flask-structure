class Venue():
    __table__ = 'venues'
    columns = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))


