import librosa
import numpy as np
import json

def analyze_audio(file_path, output_path):
   y, sr = librosa.load(file_path, sr=None)
   onset_env = librosa.onset.onset_strength(y=y, sr=sr)
   times = librosa.times_like(onset_env, sr=sr)

   onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
   onset_times = librosa.frames_to_time(onset_frames, sr=sr)

   S = np.abs(librosa.stft(y))
   freqs = librosa.fft_frequencies(sr=sr)

   bass_times = []
   snare_times = []

   for frame in onset_frames:
       spectrum = S[:, frame]
       time = librosa.frames_to_time(frame, sr=sr)

       bass_energy = spectrum[freqs < 150].sum()
       snare_energy = spectrum[(freqs >= 150) & (freqs < 2500)].sum()

       if bass_energy > snare_energy * 1.5:
           bass_times.append(round(float(time), 2))
       elif snare_energy > bass_energy * 1.5:
           snare_times.append(round(float(time), 2))

   rhythm_data = {
       "bass": bass_times,
       "snare": snare_times
   }

   with open(output_path, 'w') as f:
       json.dump(rhythm_data, f, indent=2)

   print(f"Saved rhythm data to {output_path}")

if __name__ == "__main__":
   file_path = input("Путь к mp3-файлу: ")
   analyze_audio(file_path, "rhythmData.json")
