from http.server import HTTPServer, BaseHTTPRequestHandler
import json

chocolates = {}
id_counter = 1

class ChocolateProduct:
    def __init__(self, product_type, weight, flavor, filling=None):
        self.product_type = product_type
        self.weight = weight
        self.flavor = flavor
        self.filling = filling

class Tablet(ChocolateProduct):
    def __init__(self, weight, flavor):
        super().__init__("tablet", weight, flavor)

class Bonbon(ChocolateProduct):
    def __init__(self, weight, flavor, filling):
        super().__init__("bonbon", weight, flavor, filling)

class Truffle(ChocolateProduct):
    def __init__(self, weight, flavor, filling):
        super().__init__("truffle", weight, flavor, filling)

class ChocolateFactory:
    @staticmethod
    def create_product(product_type, weight, flavor, filling=None):
        if product_type == "tablet":
            return Tablet(weight, flavor)
        elif product_type == "bonbon":
            return Bonbon(weight, flavor, filling)
        elif product_type == "truffle":
            return Truffle(weight, flavor, filling)
        else:
            raise ValueError("Tipo de producto de chocolate no válido")

class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))

class ChocolateService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_product(self, data):
        product_type = data.get("product_type", None)
        weight = data.get("weight", None)
        flavor = data.get("flavor", None)
        filling = data.get("filling", None)
        
        chocolate_product = self.factory.create_product(product_type, weight, flavor, filling)
        
        chocolates[new_id] = chocolate_product
        return chocolate_product

    def list_products(self):
        return {index: product.__dict__ for index, product in chocolates.items()}

    def update_product(self, product_id, data):
        if product_id in chocolates:
            product = chocolates[product_id]
            weight = data.get("weight", None)
            flavor = data.get("flavor", None)
            filling = data.get("filling", None)
            if weight:
                product.weight = weight
            if flavor:
                product.flavor = flavor
            if filling:
                product.filling = filling
            return product
        else:
            raise ValueError("Producto de chocolate no encontrado")

    def delete_product(self, product_id):
        if product_id in chocolates:
            del chocolates[product_id]
            return {"message": "Producto de chocolate eliminado"}
        else:
            raise ValueError("Producto de chocolate no encontrado")

class ChocolateRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chocolate_service = ChocolateService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.add_product(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_service.list_products()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            product_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            try:
                response_data = self.chocolate_service.update_product(product_id, data)
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            except ValueError as e:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": str(e)}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            product_id = int(self.path.split("/")[-1])
            try:
                response_data = self.chocolate_service.delete_product(product_id)
                HTTPDataHandler.handle_response(self, 200, response_data)
            except ValueError as e:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": str(e)}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()