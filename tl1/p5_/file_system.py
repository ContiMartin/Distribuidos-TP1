import os

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

    def read_file(self, path, offset, cant_bytes):
        try:
            if path not in self._file_manager:
                _file = open(path, "rb")
                self._file_manager[path] = _file
            else:
                _file = self._file_manager[path]
            _file.seek(offset)
            bytes_leidos = _file.read(cant_bytes)
            return bytes_leidos
        except Exception as e:
            print(' ')
            print("ERROR en Read File!!! ", e)
            return None