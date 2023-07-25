import os, pickle, numpy, glob
import tensorflow as tf
from music21 import converter, instrument, note, chord
from tqdm import tqdm
from keras.utils import to_categorical

def get_file(): # Return all data of midi file in './Data/'
    all_midi = []
    filepath = "./Data/"
    
    
    print("\nData loading...\n")
    for file in tqdm(os.listdir(filepath)):
        if file[-4:] == ".mid": 
            midi = converter.parse(filepath + file) # get data from midi file
            all_midi.append(midi)
        else:
            print("Ignore ", file)

    return all_midi

def get_sequencies(notes, n_vocab, sequence_length=100): # return network input and output, and split all notes in sequencies
    # sort and just keep unique notes
    unique_notes = sorted(set(notes))

    # dict that contains each unique note and his label
    dict_notes_label = dict((note, label) for label, note in enumerate(unique_notes))

    network_input = []
    network_output = []

    for i in range(0, len(notes) - sequence_length):
        sequence_input = notes[i:i + sequence_length]
        sequence_output = notes[i + sequence_length]
        network_input.append([dict_notes_label[element] for element in sequence_input]) # add each sequence to network input 
        network_output.append(dict_notes_label[sequence_output]) # add each end note of sequence to network output

    nb_sequences = len(network_input)
    network_input = numpy.reshape(network_input, (nb_sequences, sequence_length, 1)) # reshape for input LSTM
    network_input = network_input / float(n_vocab) # normalize input
    network_output = to_categorical(network_output) # apply one hot encoding on network output

    return network_input, network_output

def get_notes():
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    notes = []

    for file in glob.glob("Data/*.mid"):
        midi = converter.parse(file)

        print("Parsing %s" % file)

        notes_to_parse = None

        try: # file has instrument parts
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse() 
        except: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
    return notes

def get_data():
    notes = get_notes()

    file = open("save/notes", "wb") # save data in binary file
    pickle.dump(notes, file)
    file.close()

    n_vocab = len(set(notes)) # number of uniques notes
    return n_vocab, get_sequencies(notes, n_vocab)