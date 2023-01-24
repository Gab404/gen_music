from keras.callbacks import ModelCheckpoint
from preprocessing import get_data
from model import create_network

def train(model, network_input, network_output, nb_epochs=100, batch_size=128):
    filepath = "./save/weights-{epoch:02d}-{loss:.4f}.hdf5" # filepath to save each checkpoint
    checkpoint = ModelCheckpoint(
        filepath,
        save_best_only=True,
        monitor='loss',
        verbose=0,
        mode='min' # to save best loss
    )
    callbacks_list = [checkpoint]

    model.fit(network_input, network_output, epochs=nb_epochs, batch_size=batch_size, callbacks=callbacks_list)

def train_network():
    n_vocab, (network_in, network_out) = get_data()
    model = create_network(network_in, n_vocab)
    train(model, network_in, network_out)

if __name__ == '__main__':
    train_network()