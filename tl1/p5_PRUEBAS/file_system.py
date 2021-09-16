import os
import dill
from collections import defaultdict

file_user_manager = defaultdict(lambda:{})


class FS:

    def __init__(self):
        self._file_manager = {}

    def list_files(self, path):
        try:
            return os.listdir(path)
        except Exception as e:
            print(' ')
            print('ERROR!!! ', e)
            return None

    def open_file(self, path):
        try:
            if path not in self._file_manager:
                _file = open(path, 'rb')
                self._file_manager[path] = _file
            return True
        except Exception as e:
            print(' ')
            print('ERROR!!! ', e)
            return False

    def close_file(self, path):
        try:
            if path in self._file_manager:
                self._file_manager[path].close()
                del self._file_manager[path]
            return True
        except Exception as e:
            print(' ')
            print('ERROR!!! ', e)
            return False

    def read_file(cliente, self, path, offset, cant_bytes):
        try:

            if cliente not in file_user_manager:
                file_user_manager[cliente][path] = None
            if path not in file_user_manager[cliente]:
                file_user_manager[cliente][path] = None
            if file_user_manager[cliente][path] is None:
                file_user_manager[cliente][path] = open(file, 'rb')
            
            #if path not in self._file_manager:
            #    _file = open(path, "rb")
                self._file_manager[path] = _file
            else:
                _file = self._file_manager[path]
            _file.seek(offset)
            bytes_leidos = _file.read(cant_bytes)
            return bytes_leidos
        except Exception as e:
            print(' ')
            print("ERROR en Read File!!! ->", e)
            return None