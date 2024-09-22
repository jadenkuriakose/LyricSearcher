import lyricsgenius



def search_lyrics():
  while True:
    artistname = input("Enter the artist's name(or type 'exit' to quit): ")
    if artistname == 'exit':
            break
        
    songtitle = input("Enter the song title: ")
    genius = lyricsgenius.Genius("YOUR_GENIUS_API_KEY")
    
    try:
        song = genius.search_song(songtitle, artistname)
        if song:
            print(f"\nLyrics for '{songtitle}' by {artistname}:\n")
            print(song.lyrics)
            print("")
        else:
            print(f"\nSong '{songtitle}' by {artistname} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_lyrics()
