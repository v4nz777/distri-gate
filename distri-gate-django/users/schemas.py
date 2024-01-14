from ninja import ModelSchema
from users.models import User, Address
from pydantic import BaseModel


class AddressSchema(ModelSchema):
    class Meta:
        model = Address
        fields = ('id','full_address_string','address_line', 'street', 'city', 'province', 'country', 'postal_code')


class AddressIn(BaseModel):
    form_address_line: str
    form_street: str
    form_city: str
    form_postal_code: str
    form_province: str
    form_country: str



class UserSchema(ModelSchema):

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name', 'full_name', 'avatar')



class PrivateUserSchema(ModelSchema):
    address: list[AddressSchema] | None = []
    address_current: AddressSchema | None = None

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','address','address_current', 'full_name', 'avatar', 'email', 'date_joined', 'contact_number')