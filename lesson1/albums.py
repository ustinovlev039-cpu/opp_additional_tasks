"""
Создай класс Album у которого есть поля

- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - это **список**

**Создай два экземпляра album_1 и album_2**

Исполнитель: Queen

Название: Killer Queen

Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica

Название: Black Album

Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:

    def __init(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.track = tracks


album_1 = Album()
album_2 = Album()

album_1.artist = "Queen"
album_1.title = "Killer Queen"
album_1.tracks = "Brighton rock", "Killer Queen", "Tenement Funster"

album_2.artist = "Metallica"
album_2.title = "Black Album"
album_2.tracks = "Enter Sandman", "Sad But True", "Holier Than Thou"


# код для проверки 
print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков