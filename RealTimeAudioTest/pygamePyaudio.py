""" Question for this file, can pygame and pyaudio play nice together? """

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
wf = wave.open("Media/WindowsRingin.wav")
p = pyaudio.PyAudio()

# interesting, this is not hit by the debugger as it's taking place in the
# native context of the vallback for more data
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # Press the a key to play a pyaudio sound
                print("a")
                stream = p.open(
                    format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback,
                )

                stream.start_stream()
        elif event.type == pygame.QUIT:
            loop = False

    screen.fill(black)
    screen.blit(titleScreen, titleScreenRect)
    pygame.display.flip()


stream.stop_stream()
stream.close()
wf.close()

p.terminate()

sys.exit()
