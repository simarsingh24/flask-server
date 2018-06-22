from app import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class ModelSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','name','_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_model', id='<id>'),
        'collection': ma.URLFor('model')
    })

class ImageUserStatusSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'imageId', 'userId', 'status', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_image_user_status', id='<id>'),
        'collection': ma.URLFor('image_user_status')
    })

class LabelSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','text', 'modelId', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_label', id='<id>'),
        'collection': ma.URLFor('label')
    })

class ImageSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','url','height','width', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_image', id='<id>'),
        'collection': ma.URLFor('image')
    })

class BoundingBoxSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','topLeftX','topLeftY','bottomRightX','bottomRightY','confidence','isTaggedByUser','isActive','userId',
            'imageId','labelId', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_bbox', id='<id>'),
        'collection': ma.URLFor('bbox')
    })
class BoundingBoxLabelTextSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','topLeftX','topLeftY','bottomRightX','bottomRightY','confidence','isTaggedByUser','isActive','userId',
            'imageId','labelId', 'text', '_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_bbox', id='<id>'),
        'collection': ma.URLFor('bbox')
    })


class IDSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ['id']

class ArticleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','attributeType','attributeValue','isTaggedByUser','userId','imageId','isActive','_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_article', id='<id>'),
        'collection': ma.URLFor('article')
    })

class ImageAnnotationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','url','_links')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_annotation_image', id='<id>'),
        'collection': ma.URLFor('annotation_image')
    })



model_schema = ModelSchema()
models_schema = ModelSchema(many=True)

image_user_status_schema = ImageUserStatusSchema()
images_users_status_schema = ImageUserStatusSchema(many=True)

bounding_box_labelText_schema = BoundingBoxLabelTextSchema()
bounding_boxes_labelTexts_schema = BoundingBoxLabelTextSchema(many=True)

label_schema = LabelSchema()
labels_schema = LabelSchema(many=True)

image_annotation_schema = ImageAnnotationSchema()
images_annotations_schema = ImageAnnotationSchema(many=True)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

bounding_box_schema = BoundingBoxSchema()
bounding_boxes_schema = BoundingBoxSchema(many=True)

id_schema = IDSchema()
ids_schema = IDSchema(many = True)
