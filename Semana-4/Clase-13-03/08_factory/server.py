from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class DeliveryServices:
    @staticmethod
    def add_delivery(data):
        vehicle_type = data.get("vehicle_type")
        return vehicle_type

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class DeliveryVehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages_delivered = 0

    

class Scout(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=5)

class Motorcycle(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=10)


class Drone(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=20)


class DeliveryFactory:
    def create_delivery_vehicle(self, vehicle_type):
        if vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "scout":
            return Scout()
        elif vehicle_type == "drone":
            return Drone()
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/delivery":
            post_data = self.read_data()
            vehicle_type = DeliveryServices.add_delivery(post_data)


            delivery_factory = DeliveryFactory()
            delivery_vehicle = delivery_factory.create_delivery_vehicle(vehicle_type)
            
            response_data = {"message": delivery_vehicle.deliver()}

            HTTPResponseHandler.handle_response(self, 200, response_data)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data

def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()