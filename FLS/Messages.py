class BaseMessage:
    id = 0

    def __init__(self, round_id, client_id):
        self.round_id = round_id
        self.client_id = client_id


class MessageCheckpoint(BaseMessage):
    id = 1
    checkpoint_bytes = bytes([])


class MessageRegisterForRound(BaseMessage):
    id = 2
    current_time = 0


class MessageAcceptRegister(BaseMessage):
    id = 3
    acceptance = False
