from api.models import Venue
def test_init_venue():
    venue = Venue(['1', '129810298', 'la famiglia', '$$',
            '4', 100, 'www.lafamig.com'])
    assert venue.name == 'la famiglia'
