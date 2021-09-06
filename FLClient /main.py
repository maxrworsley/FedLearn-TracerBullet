import ServerConnection as ConHand
from Common import CheckpointHandler as CheckpointHandler, TFHandler
from FLS import Messages, Serialiser


def setup_handlers():
    connection = ConHand.ServerConnection("127.0.0.1", 32000)
    checkpoint = CheckpointHandler.CheckpointHandler("./Client")
    tensor_flow = TFHandler.TFHandler("./Client/model")

    return connection, checkpoint, tensor_flow


if __name__ == '__main__':
    # Connect to server and wait for model data
    server_connection, checkpoint_handler, tf_handler = setup_handlers()

    server_connection.connect()
    print("Waiting for model")
    serialised_checkpoint_bytes = server_connection.receive_data()

    checkpoint_message = Serialiser.Serialiser.deserialise_message(serialised_checkpoint_bytes)
    checkpoint_handler.save_unpack_checkpoint(checkpoint_message.checkpoint_bytes)

    print("Training Model")

    tf_handler.load_model()

    print("Sending model back")
    message_checkpoint = Messages.MessageCheckpoint(1, 1)
    message_checkpoint.checkpoint_bytes = checkpoint_handler.get_saved_checkpoint_bytes()
    serialised_checkpoint_bytes = Serialiser.Serialiser.serialise_message(message_checkpoint)

    server_connection.send_data(serialised_checkpoint_bytes)
    server_connection.close()
