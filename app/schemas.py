from app import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class ModelSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','name','_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('model_detail', id='<id>'),
        'collection': ma.URLFor('model')
    })

class ImageUserStatus(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','status')

class LabelSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','text')

class ImageSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','url')

class BoundingBoxSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','topLeftX','topLeftY','bottomRightX','bottomRightY','confidence','mode','status')




model_schema = ModelSchema()
models_schema = ModelSchema(many=True)

image_user_status_schema = ImageUserStatus()
images_users_status_schema = ImageUserStatus(many=True)


label_schema = LabelSchema()
labels_schema = LabelSchema(many=True)

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

bounding_box_schema = BoundingBoxSchema()
bounding_boxes_shema = BoundingBoxSchema(many=True)
