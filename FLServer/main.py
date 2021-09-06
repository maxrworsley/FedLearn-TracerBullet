import ClientConnection as ConHand
from Common import CheckpointHandler as CheckpointHandler
from Common import TFHandler
from FLS import Messages, Serialiser
import os


def setup_handlers():
    connection = ConHand.ClientConnection("", 32000)
    checkpoint = CheckpointHandler.CheckpointHandler("./Server")
    tensor_flow = TFHandler.TFHandler("./Server/model")

    return connection, checkpoint, tensor_flow


def make_checkpoint(checkpoint_handler, TF_handler):
    TF_handler.make_model()
    TF_handler.save_model()
    checkpoint_handler.create_checkpoint()

    message_checkpoint = Messages.MessageCheckpoint(1, 1)
    message_checkpoint.checkpoint_bytes = checkpoint_handler.get_saved_checkpoint_bytes()

    return Serialiser.Serialiser.serialise_message(message_checkpoint)


if __name__ == '__main__':
    print(f'Working from {os.getcwd()}')

    print("Serving")
    client_connection, checkpoint_handler, TF_handler = setup_handlers()

    client_connection.accept_local()
    serialised_checkpoint_message = make_checkpoint(checkpoint_handler, TF_handler)

    print("Sending checkpoint")
    client_connection.send_data(serialised_checkpoint_message)

    received_serialised_checkpoint = client_connection.receive_data()
    received_checkpoint_message = Serialiser.Serialiser.deserialise_message(received_serialised_checkpoint)

    print("Checkpoint received back, unpacking")
    checkpoint_handler.save_unpack_checkpoint(received_checkpoint_message.checkpoint_bytes)
