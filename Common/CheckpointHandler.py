import os
import shutil
from pathlib import Path


class CheckpointHandler:
    checkpoint_save_directory = ""
    checkpoint_full_path = ""

    def __init__(self, working_directory):
        self.checkpoint_save_directory = working_directory
        self.checkpoint_full_path = working_directory + "/model_checkpoint.zip"
        Path(working_directory).mkdir(parents=True, exist_ok=True)

    def create_checkpoint(self):
        owd = os.getcwd()
        try:
            os.chdir(self.checkpoint_save_directory)
            print(shutil.make_archive("model_checkpoint", "zip", "./model"))
        finally:
            os.chdir(owd)

    def get_saved_checkpoint_bytes(self):
        with open(self.checkpoint_full_path, "rb") as read_file:
            return read_file.read()

    def get_checkpoint_path(self):
        return self.checkpoint_full_path

    def save_unpack_checkpoint(self, checkpoint_bytes):
        with open(self.checkpoint_full_path, mode='wb') as newFile:
            newFile.write(checkpoint_bytes)

        self.unpack_checkpoint()

    def unpack_checkpoint(self):
        owd = os.getcwd()

        try:
            os.chdir(self.checkpoint_save_directory)
            shutil.unpack_archive("model_checkpoint.zip", "./model")
        finally:
            os.chdir(owd)
