class MusicTracker:
    def __init__(self):
        """
        Sets up the object. Which initialises an empty list
        which will be a a list of tuples of artist and song title
        params: none
        """
        self.tracks = []

    def add(self, artist, song):
        """"
        Adds a track to the list to show it has been
        listened to
        params: 
            artist - the name of the artist - str
            song - title of the song - str
        returns:
            None
        """
        if artist.strip() == '' or song.strip() == '':
            raise Exception("Artist of song can't be empty")
        
        self.tracks.append( (artist, song) )


    def list_tracks(self):
        """
        Lists all the tracks which have been added
        params: nothing
        returns: List of tracks formatted into a string
            separated by newlines '{artist}: {song}' """
        if not self.tracks:
            raise Exception("No tracks have been added yet")
        return '\n'.join([f"{track[0]}: {track[1]}" for track in self.tracks])