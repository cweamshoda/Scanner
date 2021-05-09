# Authorization key DONE
# Access granted/denied DONE
# Granted/denied audio DONE
# Termination key DONE
# Rasperry Pi INC.
# Lock connection INC.

def main():
    import vlc
    import time

    granted_audio = vlc.MediaPlayer("audio/entity_cardlock_granted.wav")
    denied_audio = vlc.MediaPlayer("audio/entity_cardlock_denied.wav")
    key = input("Enter authorization key: ")

    # Work in progress
    if key.startswith("%"):
        if key == "%KOKOPOP202?":
            print("Authorization granted.")
            granted_audio.play()
            time.sleep(1)
        else:
            print("Authorization denied.")
            denied_audio.play()
            time.sleep(1)
    elif key == "rhydonium".lower():
        print("Terminating session.")
        granted_audio.play()
        time.sleep(1)
        exit()
    else:
        print("Invalid authorization key.")
        denied_audio.play()
        time.sleep(1)

    if key.isprintable():
        time.sleep(5)
        main()


main()
