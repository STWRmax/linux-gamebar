import os

def change_volume(step):
    if step > 0:
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ +{step}%")
    else:
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ {step}%")
