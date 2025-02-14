import pulsectl

class AudioControl:
    @staticmethod
    def get_current_volume(app_name=None):
        with pulsectl.Pulse('gamebar-audio') as pulse:
            if app_name:
                for sink in pulse.sink_input_list():
                    if sink.proplist.get('application.name') == app_name:
                        return round(sink.volume.value_flat * 100)
            else:
                sink = pulse.get_sink_by_name('@DEFAULT_SINK@')
                return round(sink.volume.value_flat * 100)
    
    @staticmethod
    def set_volume(volume_percent, app_name=None):
        with pulsectl.Pulse('gamebar-audio') as pulse:
            volume = volume_percent / 100
            if app_name:
                for sink in pulse.sink_input_list():
                    if sink.proplist.get('application.name') == app_name:
                        pulse.volume_set_all_chans(sink, volume)
            else:
                sink = pulse.get_sink_by_name('@DEFAULT_SINK@')
                pulse.volume_set_all_chans(sink, volume)