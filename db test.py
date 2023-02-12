import sqlite3


class Cursor:
    def __init__(self):
        self.connection = sqlite3.connect("brick_game_maps.db")

    def add_info(self, info):
        pass

    def get_info(self, type_info='all', name_file='test'):
        if type_info == 'all':
            request = f'SELECT map_name, key, creater FROM maps WHERE map_name = "{name_file}"'
            res = self.connection.cursor().execute(request).fetchall()
        elif type_info == 'key':
            request = f'SELECT key FROM maps WHERE map_name = "{name_file}"'
            res = self.connection.cursor().execute(request).fetchall()
            res = ' '.join(res[0])
        elif type_info == 'creater':
            request = f'SELECT creater FROM maps WHERE map_name = "{name_file}"'
            res = self.connection.cursor().execute(request).fetchall()
        return res

    def get_map(self, map_name, form='list'):
        sym = ["0", "@", "*", "#", '&', '^', '%', '!', '/', '<', '>', '?']
        format_sym = [[0, 0], [-1, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]
        map_key = self.get_info("key", map_name)
        map_file = open(map_key, encoding='utf8')
        map_coded = map_file.read()
        map_uncoded = []
        for i in map_coded:
            symbol_index = sym.index(i)
            map_uncoded.append(format_sym[symbol_index])
        return map_uncoded

obj = Cursor()
print(obj.get_map("test"))
