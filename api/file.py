import hashlib,base64
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
    
    def GetFiledata(self, _file):
        with open(_file, 'rb') as filedata:   
            return base64.b64encode(filedata.read()).decode('utf-8')

    def BuildFileMd5(self):
        self.dirstr = {
            "libs": {
                "libfbconn_linux_amd64.so": {
                    "data": File.GetFiledata("./ToolDeltaServer/api/file/libs/libfbconn_linux_amd64.so"),
                    "md5": File.GetFileMd5("./ToolDeltaServer/api/file/libs/libfbconn_linux_amd64.so")
                },
                "libfbconn_windows_x86_64.dll": {
                    "data": File.GetFiledata("./ToolDeltaServer/api/file/libs/libfbconn_windows_x86_64.dll"),
                    "md5": File.GetFileMd5("./ToolDeltaServer/api/file/libs/libfbconn_windows_x86_64.dll")
                }
            }
        }
        self.api()

    def api(self):
        app = Flask(__name__)

        @app.route('/api/file', methods=['POST','GET'])
        def api():
            return jsonify(self.dirstr)

        app.run(port=8090)

if __name__ == '__main__':
    File = File()
    File.BuildFileMd5()
