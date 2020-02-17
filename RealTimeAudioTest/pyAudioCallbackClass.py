""" Question for this file, can I create a class with a pyaudio callback? """

# pylint: disable=no-member

import sys, pygame
import pyaudio, wave, time

pygame.init()

size = width, height = 240, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

titleScreen = pygame.image.load("Media/Screen.png")
titleScreenRect = titleScreen.get_rect()

# audio init
p = pyaudio.PyAudio()


class audio_class:
    def __init__(self):
        self.started = False
        self.start_frame = -1
        self.wf = wave.open("Media/WindowsRingin.wav")
        self.stream = p.open(
            format=p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True,
            stream_callback=self.callback,
        )

        self.stream.start_stream()

    def callback(self, in_data, frame_count, time_info, status):
        print(str(frame_count))
        data = self.wf.readframes(frame_count)
        # return (data, pyaudio.paContinue)

        # Note: returning None is killing the stream, need a different way to do this
        return (None, pyaudio.paContinue)

    # def callback(self, in_data, frame_count, time_info, status):
    # print(str(frame_count))
    # if self.started:
    # data = self.wf.readframes(frame_count)
    # return (data, pyaudio.paContinue)

    # return (None, pyaudio.paContinue)

    def start(self):
        self.started = True

    def close(self):
        self.wf.close()
        self.stream.stop_stream()
        self.stream.close()


# Create our class
audio = audio_class()

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # Press the a key to play a pyaudio sound
                audio.start()
        elif event.type == pygame.QUIT:
            loop = False

    screen.fill(black)
    screen.blit(titleScreen, titleScreenRect)
    pygame.display.flip()

audio.close()

p.terminate()

sys.exit()
