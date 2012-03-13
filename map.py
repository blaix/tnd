class Map(object):
    """
    Initialize with a tilemap string:
    (g is grass, w is water)
    
    >>> tilemap = \"""
    ... w w g g g g g g g g
    ... g w w g g g g g g g
    ... g g w w g g g g g g
    ... g g g w w g g g g g
    ... g g g g w w g g g g
    ... g g g g g w w g g g
    ... g g g g g g w w g g
    ... g g g g g g g w w g
    ... \"""
    >>> map = Map(tilemap)
    >>> map.tiles
    [['w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
    ['g', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
    ['g', 'g', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g']
    ['g', 'g', 'g', 'w', 'w', 'g', 'g', 'g', 'g', 'g']
    ['g', 'g', 'g', 'g', 'w', 'w', 'g', 'g', 'g', 'g']
    ['g', 'g', 'g', 'g', 'g', 'w', 'w', 'g', 'g', 'g']
    ['g', 'g', 'g', 'g', 'g', 'g', 'w', 'w', 'g', 'g']
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'w', 'w', 'g']]
    
    TODO: make it work... make it useful...
    """
    pass

class Tile(object):
    pass