# Authorization key DONE
# Access granted/denied DONE
# Granted/denied audio PARTIAL
# Rasperry Pi INC.
# Lock connection INC.

import vlc
import time

granted_audio = vlc.MediaPlayer("audio/granted.wav")
denied_audio = vlc.MediaPlayer("audio/denied.wav")

key = input("Enter authorization key: ")

# Work in progress
if key == "%KOKOPOP202?":
    print("Authorization granted.")
    granted_audio.play()
    time.sleep(4)
else:
    print("Authorization denied.")
