#modules import
import sounddevice as sd
import soundfile as sf
import time
from threading import Thread


#A class for playing audio files
class AudioPlayer:
    """A class for playing audio files.
    Attributes:
        file_path (str): The path to the audio file to be played.
        device (int, optional): The index of the sound device to use. Defaults set to None, which uses the default system device.
        data (numpy array): The audio data read from the file.
        sample_rate (int): The sample rate of the audio data.
        total_time (float): The total duration of the audio file in seconds.
        current_time (float): The current playback time in seconds.
        is_playing (bool): Whether or not the audio is currently playing.
    """
    #constructor
    def __init__(self, file_path, device=None):
        """Initializes an AudioPlayer object.
        Args:
            file_path (str): The path to the audio file to be played.
            device (int, optional): The index of the sound device to use. Defaults set to None, which uses the default system device.
        """
        #variables
        self.file_path = file_path
        self.data, self.sample_rate = sf.read(file_path, dtype='float32')
        self.total_time = len(self.data) / self.sample_rate
        self.current_time = 0
        self.is_playing = False
        self.device = device


    #play the audio file and update the current time
    def play(self):
        """Starts playing the audio file from the current time and update the current time every 0.5 seconds.
        """
        if not self.is_playing:
            self.is_playing = True
            Thread(target=self.play_audio, ).start()
            Thread(target=self.update_time, daemon=True).start()
    
    #Plays the audio file.
    def play_audio(self):
        """Plays the audio file.
        """
        if self.device is not None:
            #play audio in chunks to improve memory use
            with sd.OutputStream(device=self.device, blocksize=2048, samplerate=self.sample_rate, channels=2) as stream:
                i = int(self.current_time * self.sample_rate)
                while self.is_playing and i < len(self.data):
                    chunk = self.data[i:i+2048]
                    stream.write(chunk)
                    i += 2048
                #reset associated parameters when the audio file terminated
                if i >= len(self.data):
                    self.stop()
        else:
            sd.play(self.data, self.sample_rate)
    
    #pause the audio file playback
    def pause(self):
        """Pauses the audio playback.
        """
        if self.is_playing:
            self.is_playing = False
    
    #stop the audio file playback
    def stop(self):
        """Stops the audio playback and resets the current time to 0.
        """
        if self.is_playing:
            self.is_playing = False
        self.current_time = 0
    
    #Rewinds the audio playback by the specified number of seconds
    def rewind(self, seconds):
        """Rewinds the audio playback by the specified number of seconds.
        Args:
            seconds (float): The number of seconds to rewind.
        """
        if self.current_time - seconds < 0:
            self.current_time = 0
        else:
            self.current_time -= seconds
    
    #Fast-forwards the audio playback by the specified number of seconds
    def fast_forward(self, seconds):
        """Fast-forwards the audio playback by the specified number of seconds.
        Args:
            seconds (float): The number of seconds to fast-forward.
        """
        if self.current_time + seconds > self.total_time:
            self.current_time = self.total_time
        else:
            self.current_time += seconds
    
    #Updates the current playback time 
    def update_time(self):
        """Updates the current playback time every 0.5 seconds.
        """
        while self.is_playing:
            time.sleep(0.1)
            self.current_time += 0.1
    
    #Returns the current time
    def get_time_passed(self):
        """Returns the current time.
        """
        return self.current_time
    
    #Calculates and returns the remaining time
    def get_time_remaining(self):
        """Calculates and returns the remaining time.
        Returns:
            The remaining time (in seconds) between the total time and the current time.
            If total time is 0, then returns 0.
        """
        if self.total_time is not 0:
            return self.total_time - self.current_time
        else:
            return 0
