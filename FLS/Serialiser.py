import pickle


class Serialiser:
    @staticmethod
    def serialise_message(message_object):
        message_bytes = pickle.dumps(message_object)
        return message_bytes

    @staticmethod
    def deserialise_message(message_bytes):
        message_object = pickle.loads(message_bytes)
        return message_object
