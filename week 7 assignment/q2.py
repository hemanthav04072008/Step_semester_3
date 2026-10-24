class Playlist:
    def __init__(self, max_songs):
        self.__songs = [None] * max_songs
        self.__count = 0
        self.__max_songs = max_songs

    def addSong(self, song):
        if self.__count < self.__max_songs:
            self.__songs[self.__count] = song
            self.__count += 1
        else:
            print("Playlist is full")

    def getSongs(self):
        return self.__songs[:self.__count].copy()

    def getSongCount(self):
        return self.__count


p = Playlist(10)
p.addSong("Song A")
p.addSong("Song B")

songs = p.getSongs()
print("Songs =", songs)

songs[0] = "Hacked"
print("Playlist songs =", p.getSongs())
print("Song count =", p.getSongCount())