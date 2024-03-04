from http.server import HTTPServer, BaseHTTPRequestHandler
import json
estudiantes = [
    {
        "id":1,
        "nombre":"Pedrito",
        "apellido":"Garcia",
        "carrera":"Ingenieria de Sistemas",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        # Agrega una ruta para mostrar todas las carreras
        elif self.path == '/carreras':
            carreras= [estudiante['carrera'] for estudiante in estudiantes]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(carreras).encode('utf-8'))
        #Agrega una ruta que devuelva a todos los estudiantes de la carrera de “Economía”
        elif self.path == '/economia':
            carrera_economia= [estudiante for estudiante in estudiantes if estudiante['carrera'] == "Economia"]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(carrera_economia).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))

    def do_DELETE(self):
        if self.path == '/estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        
    def do_POST(self):
        if self.path == '/estudiantes':
            content_length = int(self.headers['Content-Length'])     
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        
        elif self.path == '/economia':
            content_length = int(self.headers['Content-Length'])     
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['carrera']= 'Economia'
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
    def do_PUT(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            id = data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(data)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8") )
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))




def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()



if __name__ == "__main__":
    run_server()