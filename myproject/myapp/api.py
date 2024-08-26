from ninja import NinjaAPI, Schema

users = NinjaAPI()

class UsersInfoSchema(Schema):
    name: str
    age: int
    email: str
    password: str
    address: str
    phone: str
    gender: str
    role: str
    status: str
    created_at: str
    updated_at: str
@users.get("/all_users", response=UsersInfoSchema)
def all_users(request):
    users = model.objects.all()
    return users