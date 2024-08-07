from globals import *
from text import Text, debug

class Music:
    def __init__(self, volume):
        self.path = (fr"{application_path}\src\music")
        self.setup(volume)
 
         
    def setup(self, volume):
        self.track_end = pygame.USEREVENT+1
        self.tracks = []
        self.track = 0
        for track in os.listdir(self.path):
            self.tracks.append(os.path.join(self.path, track))
        random.shuffle(self.tracks)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.set_endevent(self.track_end)
        pygame.mixer.music.load(self.tracks[0])
        pygame.mixer.music.play()

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
            