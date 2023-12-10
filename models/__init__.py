#!/usr/bin/env python3
""" import modules for creating a unique Filestorage """

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
