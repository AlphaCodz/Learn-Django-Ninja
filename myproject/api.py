from ninja import NinjaAPI, Schema

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

# Parsing Input
@api.get("/hi")
def hello_name(request, name):
    return f"Hello {name}"

# Specify a default value for argument
@api.get("/default_value")
def spec_def_value(request, name="alpha"):
    return f"Hello {name}"


# Type Hinting
@api.get("/type_hint")
def type_hinting(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}


# Input from path
@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}


# Input from request body
class HelloSchema(Schema):
    name: str = "world"
    
@api.post("/hello_request")
def hello_from_request_body(request, data: HelloSchema):
    return f"Hello {data.name}"

