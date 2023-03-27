class AudioPlayer:
    def __init__(self, file_path, device=None):
        self.file_path = file_path
        self.data, self.sample_rate = sf.read(file_path, dtype='float32')
        self.total_time = len(self.data) / self.sample_rate
        self.current_time = 0
        self.is_playing = False
        self.device = device
    
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            Thread(target=self.play_audio, ).start()
            Thread(target=self.update_time, args=(), daemon=True).start()
    
    def play_audio(self):
        if self.device is not None:
            with sd.OutputStream(device=self.device, blocksize=2048, samplerate=self.sample_rate, channels=1) as stream:
                i = 0
                while self.is_playing and i < len(self.data):
                    chunk = self.data[i:i+2048]
                    stream.write(chunk)
                    i += 2048
        else:
            sd.play(self.data, self.sample_rate)
    
    def pause(self):
        if self.is_playing:
            self.is_playing = False
    
    def stop(self):
        if self.is_playing:
            self.is_playing = False
        self.current_time = 0
    
    def rewind(self, seconds):
        if self.current_time - seconds < 0:
            self.current_time = 0
        else:
            self.current_time -= seconds
    
    def fast_forward(self, seconds):
        if self.current_time + seconds > self.total_time:
            self.current_time = self.total_time
        else:
            self.current_time += seconds
    
    def update_time(self):
        while self.is_playing:
            time.sleep(1)
            self.current_time += 1
    
    def get_time_passed(self):
        return self.current_time
    
    def get_time_remaining(self):
        if self.total_time is not 0:
            return self.total_time - self.current_time
        else:
            return 0
