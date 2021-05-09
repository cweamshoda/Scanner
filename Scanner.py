# Authorization key DONE
# Access granted/denied DONE
# Granted/denied audio DONE
# Termination key DONE
# System lockdown INC.
# Raspberry Pi INC.
# Lock connection INC.
import vlc
import time

failed_attempts = 0


def main():
    granted_audio = vlc.MediaPlayer("audio/entity_cardlock_granted.wav")
    denied_audio = vlc.MediaPlayer("audio/entity_cardlock_denied.wav")
    # terminated_audio
    global failed_attempts

    key = input("Enter authorization key: ")

    # Work in progress
    if failed_attempts == 3:
        print("System lockdown initiated")
        time.sleep(5)
        failed_attempts = 0
        print("System lockdown disabled.")
    if key.startswith("%"):
        if key == "%KOKOPOP202?":
            print("Authorization granted.")
            granted_audio.play()
            time.sleep(1)
        else:
            print("Authorization denied.")
            denied_audio.play()
            failed_attempts = failed_attempts + 1
            time.sleep(1)
    elif key == "rhydonium".lower():
        print("Terminating session.")
        granted_audio.play()
        time.sleep(1)
        exit()
    else:
        print("Invalid authorization key.")
        denied_audio.play()
        failed_attempts = failed_attempts + 1
        time.sleep(1)
    if key.isprintable():
        time.sleep(2)
        main()


main()
