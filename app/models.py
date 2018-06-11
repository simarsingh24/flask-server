from app import db

class BoundingBox(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    topLeftX = db.Column(db.Float)
    topLeftY = db.Column(db.Float)
    bottomRightX = db.Column(db.Float)
    bottomRightY = db.Column(db.Float)
    confidence = db.Column(db.Float)
    mode = db.Column(db.Boolean)
    status = db.Column(db.Boolean)
    userId = db.Column(db.Integer,nullable=False)
    imageId=db.Column(db.Integer,db.ForeignKey('image.id'),nullable=False)
    labelId=db.Column(db.Integer,db.ForeignKey('label.id'),nullable=False)
  
    def __init__(self, topLeftX,topLeftY,bottomRightX,bottomRightY,confidence,mode,status,userId,imageId,labelId):
        self.topLeftY = topLeftY
        self.topLeftX = topLeftX
        self.bottomRightY =bottomRightY
        self.bottomRightX = bottomRightX
        self.confidence = confidence
        self.mode = mode
        self.status = status
        self.userId = userId
        self.imageId = imageId
        self.labelId = labelId

    def __repr__(self):
        return '<BoundingBox {}>'.format(self.id)  

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    url = db.Column(db.String(2083),nullable = False)
    boundingbox = db.relationship('BoundingBox', backref='image', lazy=True)
    imageuserstatus = db.relationship('ImageUserStatus', backref='image', lazy=True)

    def __init__(self, url):
        self.url = url
    
    def __repr__(self):
        return '<Image {}>'.format(self.id)  

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    text = db.Column(db.String(80))
    modelId = db.Column(db.Integer,db.ForeignKey('model.id'),nullable=False)
    
    boundingbox = db.relationship('BoundingBox', backref='label', lazy=True)

    def __init__(self, text,modelId):
        self.text = text
        self.modelId = modelId

    def __repr__(self):
        return '<Label {}>'.format(self.id)  

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    label = db.relationship('Label', backref='model', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model {}>'.format(self.id)  

class ImageUserStatus(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    status = db.Column(db.String(10))
    imageId=db.Column(db.Integer,db.ForeignKey('image.id'),nullable=False)
    userId = db.Column(db.Integer,nullable=False)

    def __init__(self, status,imageId,userId):
        self.status= status
        self.imageId = imageId
        self.userId = userId

    def __repr__(self):
        return '<ImageUserStatus {}>'.format(self.id)  

db.create_all()
