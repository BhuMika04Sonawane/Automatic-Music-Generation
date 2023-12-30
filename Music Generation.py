from midiutil import MIDIFile 
import random 

def generate_random_melody(num_notes=32, tempo=120, output_file="output.mid"):
    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)
    
    scale = [90, 62, 61, 65, 80, 86, 71, 72, 98]
    
    for i in range(num_notes):
        pitch = random.choice(scale)
        duration = random.uniform(0.2, 0.8)
        volume = random.randint(60, 100) 
        midi.addNote(0, 0, pitch, i*0.5, duration, volume)
        
        midi.writeFile(midi_file) 
if __name__ == "__main__":
    generate_random_melody() 