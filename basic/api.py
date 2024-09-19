from ninja import Router, Schema

"""
A schema is used to define the structure and validation rules for data that your API accepts or returns. Schemas are based on Pydantic models, which allow you to define data types, set default values, and validate input data.
"""

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None
    first_name: str = None
    last_name: str = None
    
class Error(Schema):
    status: int = 403
    message: str

basic_router = Router()


@basic_router.get("/signup", response=UserSchema)
def me(request):
    return request.user
    # In django ninja if no authentication is configured, request.user will be an instance of AnonymousUser (by default), hence in this case the UserSchema data will be returned instead of an AnonymouseUser error


# Multiple response types
@basic_router.get("/me", response={200: UserSchema, 403: Error})
def authenticated_user(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user