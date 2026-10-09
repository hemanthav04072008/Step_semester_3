class Playlist:
    def __init__(self, max_size):
        self.__songs = [None] * max_size
        self.__count = 0

    def addSong(self, song):
        if self.__count < len(self.__songs):
            self.__songs[self.__count] = song
            self.__count += 1

    def getSongs(self):
        return self.__songs[:self.__count].copy()

    def getSongCount(self):
        return self.__count


p = Playlist(10)
p.addSong("Song A")
p.addSong("Song B")

songs = p.getSongs()
print(songs)

songs[0] = "Hacked"
print(p.getSongs())
print(p.getSongCount())