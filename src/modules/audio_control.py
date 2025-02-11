import subprocess

def list_audio_apps():
    result = subprocess.run(["pactl", "list", "sink-inputs"], capture_output=True, text=True)
    apps = []
    for line in result.stdout.split("\n"):
        if "application.name" in line:
            app_name = line.split("=")[1].strip('"')
            apps.append(app_name)
    return apps

def change_volume(amount):
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{amount}%"])

def change_app_volume(app_id, amount):
    subprocess.run(["pactl", "set-sink-input-volume", str(app_id), f"{amount}%"])