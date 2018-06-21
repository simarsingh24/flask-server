from flask import request, redirect, url_for,jsonify
from app import app, db
from app.models import *
from app.schemas import *
import requests

@app.route('/')
def home():
	return "home"

## CRUD

# Model

#CREATE AND GET ALL
@app.route('/model' , methods=['POST', 'GET'])
def model():
	if request.method == 'POST':
		name = request.json["name"]
		new_model = Model(name)
		db.session.add(new_model)
		db.session.commit()
		return model_schema.jsonify(new_model)	
	if request.method == 'GET' :
		all_model = Model.query.all()
		result = models_schema.dump(all_model)
		return jsonify(result.data)

#UPDATE
@app.route('/model/<id>', methods = ['PUT'])
def update_model(id):
    model = Model.query.get(id)
    model.name = request.json["name"]
    db.session.commit()
    return model_schema.jsonify(model)

#DELETE
@app.route('/model/<id>', methods = ['DELETE'])
def delete_model(id):
    model = Model.query.get(id)
    db.session.delete(model)
    db.session.commit()
    return model_schema.jsonify(model)

#GET BY ID
@app.route('/model/<id>')
def get_model(id):
    model = Model.query.get(id)
    return model_schema.jsonify(model)

# Image

#CREATE AND GET ALL
@app.route('/image' , methods=['POST', 'GET'])
def image():
    if request.method == 'POST':
        url = request.json["url"]
        height = request.json["height"]
        width = request.json["width"]

        new_image = Image(url,height,width)
        db.session.add(new_image)
        db.session.commit()
        return image_schema.jsonify(new_image)  
    if request.method == 'GET' :
        all_image = Image.query.all()
        result = images_schema.dump(all_image)
        return jsonify(result.data)

#UPDATE
@app.route('/image/<id>', methods = ['PUT'])
def update_image(id):
    image = Image.query.get(id)
    image.url = request.json["url"]
    image.height = request.json["height"]
    image.width = request.json["width"]
    db.session.commit()
    return image_schema.jsonify(image)

#DELETE
@app.route('/image/<id>', methods = ['DELETE'])
def delete_image(id):
    image = Image.query.get(id)
    db.session.delete(image)
    db.session.commit()
    return image_schema.jsonify(image)

#GET BY ID
@app.route('/image/<id>')
def get_image(id):
    image = Image.query.get(id)
    return image_schema.jsonify(image)


# Image User Status

#CREATE AND READ ALL
@app.route('/image_user' , methods=['POST', 'GET'])
def image_user_status():
    if request.method == 'POST':
        user_id = request.json["user_id"]
        image_id = request.json["image_id"]
        status = request.json["status"]
        new_image_user = ImageUserStatus(status, image_id, user_id)
        db.session.add(new_image_user)
        db.session.commit()
        return image_user_status_schema.jsonify(new_image_user)  
    if request.method == 'GET' :
        all_image_user = ImageUserStatus.query.all()
        result = images_users_status_schema.dump(all_image_user)
        return jsonify(result.data)

#UPDATE
@app.route('/image_user/<id>', methods = ['PUT'])
def update_image_user_status(id):
    image_user = ImageUserStatus.query.get(id)
    image_user.status = request.json["status"]
    image_user.userId = request.json["user_id"]
    image_user.imageId = request.json["image_id"]
    db.session.commit()
    return image_user_status_schema.jsonify(image_user)

#DELETE
@app.route('/image_user/<id>', methods = ['DELETE'])
def delete_image_user_status(id):
    image_user = ImageUserStatus.query.get(id)
    db.session.delete(image_user)
    db.session.commit()
    return image_user_status_schema.jsonify(image_user)

#GET BY ID
@app.route('/image_user/<id>')
def get_image_user_status(id):
    image_user = ImageUserStatus.query.get(id)
    return image_user_status_schema.jsonify(image_user)


# Label

#CREATE AND GET ALL
@app.route('/label' , methods=['POST', 'GET'])
def label():
    if request.method == 'POST':
        text = request.json["text"]
        model_id = request.json["model_id"]
        new_label = Label(text, model_id)
        db.session.add(new_label)
        db.session.commit()
        return label_schema.jsonify(new_label)  
    if request.method == 'GET' :
        all_label = Label.query.all()
        result = labels_schema.dump(all_label)
        return jsonify(result.data)

#UPDATE
@app.route('/label/<id>', methods = ['PUT'])
def update_label(id):
    label = Label.query.get(id)
    label.text = request.json["text"]
    label.modelId = request.json["model_id"]
    db.session.commit()
    return label_schema.jsonify(label)

#DELETE
@app.route('/label/<id>', methods = ['DELETE'])
def delete_label(id):
    label = Label.query.get(id)
    db.session.delete(label)
    db.session.commit()
    return label_schema.jsonify(label)

#GET BY ID
@app.route('/label/<id>')
def get_label(id):
    label = Label.query.get(id)
    return label_schema.jsonify(label)


# Bounding Box

#CREATE AND GET ALL
@app.route('/bbox' , methods=['POST', 'GET'])
def bbox():
    if request.method == 'POST':
        bbox_tlx = request.json["topLeftX"]
        bbox_tly = request.json["topLeftY"]
        bbox_brx = request.json["bottomRightX"]
        bbox_bry = request.json["bottomRightY"]
        confidence = request.json["confidence"]
        isTaggedByUser = request.json["isTaggedByUser"]
        isActive = request.json["isActive"]
        user_id = request.json["userId"]
        image_id = request.json["imageId"]
        label_id = request.json["labelId"]
        new_bbox = BoundingBox(bbox_tlx,bbox_tly,bbox_brx,bbox_bry,confidence,
            isTaggedByUser,isActive,user_id,image_id,label_id)
        db.session.add(new_bbox)
        db.session.commit()
        return bounding_box_schema.jsonify(new_bbox)  
    if request.method == 'GET' :
        all_bbox = BoundingBox.query.all()
        result = bounding_boxes_schema.dump(all_bbox)
        return jsonify(result.data)

#UPDATE
@app.route('/bbox/<id>', methods = ['PUT'])
def update_bbox(id):
    bbox = BoundingBox.query.get(id)
    bbox.topLeftX = request.json["topLeftX"]
    bbox.topLeftY = request.json["topLeftY"]
    bbox.bottomRightX = request.json["bottomRightX"]
    bbox.bottomRightY = request.json["bottomRightY"]
    bbox.confidence = request.json["confidence"]
    bbox.isTaggedByUser = request.json["isTaggedByUser"]
    bbox.isActive = request.json["isActive"]
    bbox.userId = request.json["userId"]
    bbox.imageId = request.json["imageId"]
    bbox.labelId = request.json["labelId"]
    db.session.commit()
    return bounding_box_schema.jsonify(bbox)

#DELETE
@app.route('/bbox/<id>', methods = ['DELETE'])
def delete_bbox(id):
    bbox = BoundingBox.query.get(id)
    db.session.delete(bbox)
    db.session.commit()
    return bounding_box_schema.jsonify(bbox)

#GET BY ID
@app.route('/bbox/<id>')
def get_bbox(id):
    bbox = BoundingBox.query.get(id)
    return bounding_box_schema.jsonify(bbox)


# GET unseen images for given userid 
@app.route('/untagged/<user_id>')
def get_untagged_images(user_id):
    limit = request.args.get('limit')
    untagged = db.engine.execute(
        "SELECT id, url ,height , width FROM (SELECT * FROM ( SELECT IMAGEID FROM IMAGE_USER_STATUS WHERE USERID = {})a RIGHT JOIN IMAGE ON IMAGE.ID = a.IMAGEID)b where IMAGEID IS NULL LIMIT %s"\
        .format(user_id),int(limit))
    result = images_schema.dump(untagged)
    return jsonify(result.data)

#GET skipped images for given userid
@app.route('/skipped/<user_id>')
def get_skipped_images(user_id):
    limit = request.args.get('limit')
    untagged = db.engine.execute(
        "SELECT id, url ,height , width FROM (SELECT * FROM ( SELECT IMAGEID FROM IMAGE_USER_STATUS WHERE USERID = {} AND STATUS=\"skipped\")a JOIN IMAGE ON IMAGE.ID = a.IMAGEID)b LIMIT %s"\
        .format(user_id),int(limit))
    result = images_schema.dump(untagged)
    return jsonify(result.data)

#List of bounding box for given image
@app.route('/bbox/image/<image_id>')
def get_bbox_filter_image(image_id):
    all_bbox = db.engine.execute(
        "SELECT BOUNDING_BOX.*, text FROM BOUNDING_BOX JOIN LABEL ON BOUNDING_BOX.LABELID = LABEL.ID WHERE BOUNDING_BOX.imageId = {}"
        .format(image_id))
    result = bounding_boxes_labelTexts_schema.dump(all_bbox)
    return jsonify(result.data)

#List of bounding boxes tagged by user or model
@app.route('/bbox/image/<image_id>/<isTaggedByUser>')
def get_bbox_filter_image_mode(image_id, isTaggedByUser):
    all_bbox = db.engine.execute(
        "SELECT BOUNDING_BOX.*, text FROM BOUNDING_BOX JOIN LABEL ON BOUNDING_BOX.LABELID = LABEL.ID WHERE BOUNDING_BOX.imageId = {} AND BOUNDING_BOX.isTaggedByUser = {}"
        .format(image_id, isTaggedByUser))
    result = bounding_boxes_labelTexts_schema.dump(all_bbox)
    return jsonify(result.data)

# Tag an image given imageid and userid,Accepts Status as a query par
@app.route('/tag/<image_id>/<user_id>', methods = ['POST'])
def tag_image(image_id, user_id):
    tag_status = request.args.get('status')
    tagger = request.args.get('modelTag')
    if int(tagger):
        try:
            image_user = ImageUserStatus(tag_status, image_id, user_id)
            db.session.add(new_image_user_status)
        except:
            image_user = ImageUserStatus.query.filter_by(userId = user_id, imageId = image_id)
            image_user.status = tag_status
        db.session.commit()
    if tag_status != 'skipped':
        all_bbox = []
        for bbox_request in request.json:
            bbox_tlx = bbox_request["topleft"]["x"]
            bbox_tly = bbox_request["topleft"]["y"]
            bbox_brx = bbox_request["bottomright"]["x"]
            bbox_bry = bbox_request["bottomright"]["y"]
            confidence = bbox_request["confidence"]
            isTaggedByUser = bbox_request["isTaggedByUser"]
            isActive = bbox_request["isActive"]
            label_id = bbox_request["labelId"]
            db.session.add(BoundingBox(bbox_tlx,bbox_tly,bbox_brx,bbox_bry,confidence,isTaggedByUser,
                isActive,user_id,image_id,label_id))
    db.session.commit()
    return jsonify(images_users_status_schema.dump(image_user).data)

# @app.route('/model_tag/<image_id>', methods = ['POST'])
# def tag_image(image_id):
#     all_bbox = []
#     for bbox_request in request.json:
#         bbox_tlx = bbox_request["topleft"]["x"]
#         bbox_tly = bbox_request["topleft"]["y"]
#         bbox_brx = bbox_request["bottomright"]["x"]
#         bbox_bry = bbox_request["bottomright"]["y"]
#         confidence = bbox_request["confidence"]
#         isTaggedByUser = bbox_request["isTaggedByUser"]
#         isActive = bbox_request["isActive"]
#         label_id = bbox_request["labelId"]
#         db.session.add(BoundingBox(bbox_tlx,bbox_tly,bbox_brx,bbox_bry,confidence,isTaggedByUser,
#             isActive,user_id,image_id,label_id))
#     db.session.commit()
#     return 'tagged'

@app.route('/label/model/<model_id>')
def get_label_filter_model(model_id):
    all_label = Label.query.filter_by(modelId = model_id)
    result = labels_schema.dump(all_label)
    return(jsonify(result.data))



















