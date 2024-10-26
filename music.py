from globals import *
from text import Text, debug

class Music:
    path = (fr"{application_path}\src\music\explore")
    volume = 0.3

    def __init__(self):
        self.setup(Music.volume)
         
    def setup(self, volume):
        self.track_end = pygame.USEREVENT+1
        self.tracks = []
        self.track = 0
        for track in os.listdir(Music.path):
            self.tracks.append(os.path.join(Music.path, track))
        random.shuffle(self.tracks)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.set_endevent(self.track_end)
        pygame.mixer.music.load(self.tracks[0])
        pygame.mixer.music.play()

    def change_path(self):
        pygame.mixer.Sound.play(TAB)
        pygame.mixer.music.fadeout(500)
        if Music.path == (fr"{application_path}\src\music\explore"):
            Music.path = (fr"{application_path}\src\music\dungeon")
            debug.text = "> Music playlist: [Dungeon]"
        else:
            Music.path = (fr"{application_path}\src\music\explore")
            debug.text = "> Music playlist: [Explore]"

        self.setup(Music.volume)

    @classmethod
    def pause(cls):
        Text.draw_tooltip(debug)
        if pygame.mixer.music.get_busy():
            pygame.mixer.Sound.play(HOLOTAPE_STOP)
            pygame.mixer.music.pause()
            debug.text = "> Music: [PAUSE]"
        else:
            pygame.mixer.Sound.play(HOLOTAPE_START)
            debug.text = "> Music: [RESUME]"
            pygame.mixer.music.unpause()
            