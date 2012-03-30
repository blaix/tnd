class Map(object):
    """
    Representation of a map of tiles.
    
    Initialize with a tilemap string:
    (where g might represent grass, w might represent water)
    
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
    >>> map.get_tiles()
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
    
    def __init__(self, tilemap):
        self.tiles = []
        for row in strip(tilemap).split("\n"):
            self.tiles.append([])
            for tile in row.split(" "):
                self.tiles[self.tiles.count() - 1].append(Tile.new(tile))
    
    def get_tiles(self):
        """
        Get a nested list representation of all tiles.
        """
        pass

class Tile(object):
    pass