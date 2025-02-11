import psutil
import speedtest

def get_fps():
    return "FPS: 60 (Simulado)"

def get_ram_usage():
    return f"RAM: {psutil.virtual_memory().percent}%"

def get_gpu_usage():
    return "GPU: 40% (Simulado)"

def get_network_speed():
    st = speedtest.Speedtest()
    download = round(st.download() / 1_000_000, 2)
    upload = round(st.upload() / 1_000_000, 2)
    return f"📥 {download} Mbps / 📤 {upload} Mbps"