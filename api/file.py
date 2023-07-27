import hashlib
from flask import Flask, jsonify, request

class File:
    def GetFileMd5(self, _file):
        with open(_file, 'rb') as filedata:
            md5_obj = hashlib.md5()
            while True:
                data = filedata.read(1024 * 4)
                if not data:
                    break
                md5_obj.update(data)
        return md5_obj.hexdigest()

    def BuildFileMd5(self):
        self.dirstr = {
            "libs": {
                "libfbconn_linux_amd64.so": {
                    "path": "./ToolDeltaServer/api/file/libs/libfbconn_linux_amd64.so",
                    "md5": File.GetFileMd5("./ToolDeltaServer/api/file/libs/libfbconn_linux_amd64.so")
                },
                "libfbconn_windows_x86_64.dll": {
                    "path": "./ToolDeltaServer/api/file/libs/libfbconn_windows_x86_64.dll",
                    "md5": File.GetFileMd5("./ToolDeltaServer/api/file/libs/libfbconn_windows_x86_64.dll")
                }
            }
        }
        self.api()

    def api(self):
        app = Flask(__name__)

        @app.route('/api/file', methods=['POST'])
        def api():
            return jsonify(self.dirstr)

        app.run(port=8090)

if __name__ == '__main__':
    File = File()
    File.BuildFileMd5()
