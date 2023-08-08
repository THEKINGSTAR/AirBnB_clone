#!/usr/bin/python3
""" __init__.py """

from models.engine.file_storage import FileStorage

storage = FileStorage()
if __name__ == "__main__":
    storage.reload()
