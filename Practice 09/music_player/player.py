import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        pygame.mixer.init()
        self.music_dir = music_dir
        if os.path.exists(music_dir):
            self.playlist = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
        else:
            self.playlist = []
            
        self.current_index = 0
        self.is_playing = False

    def play(self):
        if not self.playlist:
            return
        
        track_path = os.path.join(self.music_dir, self.playlist[self.current_index])
        try:
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            self.is_playing = True
        except pygame.error:
            pass

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def get_current_track_name(self):
        if self.playlist:
            return self.playlist[self.current_index]
        return "Empty Playlist"

    def get_pos(self):
        if self.is_playing:
            return pygame.mixer.music.get_pos() // 1000
        return 0