from postscraper import db


class PostUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class PostText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post_url.id', ondelete='CASCADE'))
    post = db.relationship('PostUrl')
    title = db.Column(db.Text(), nullable=True)
    text = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)