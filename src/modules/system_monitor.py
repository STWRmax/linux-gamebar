import psutil
import py3nvml.py3nvml as nvml

class SystemMonitor:
    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent(interval=1)
    
    @staticmethod
    def get_ram_usage():
        return psutil.virtual_memory().percent
    
    @staticmethod
    def get_gpu_usage():
        try:
            nvml.nvmlInit()
            handle = nvml.nvmlDeviceGetHandleByIndex(0)
            util = nvml.nvmlDeviceGetUtilizationRates(handle)
            return util.gpu
        except:
            return 0  # Si no hay GPU NVIDIA
        
    @staticmethod
    def get_network_speed():
        net_io = psutil.net_io_counters()
        return {
            "upload": net_io.bytes_sent,
            "download": net_io.bytes_recv
        }