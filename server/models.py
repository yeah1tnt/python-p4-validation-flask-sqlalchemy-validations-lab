from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    

    @validates('name')
    def validate_name(self, key, name):
        names = db.session.query(Author).filter_by(name=name).all()
        if names in names:
            raise ValueError(f'Name {name} already exists')
        elif name == '':
            raise ValueError(f'Name cannot be empty')
        else:
            return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        phone_numbers = db.session.query(Author).filter_by(phone_number=phone_number).all()
        if phone_numbers in phone_numbers:
            raise ValueError(f'Phone number {phone_number} already exists')
        elif len(phone_number) != 10:
            raise ValueError(f'Phone number must be 10 digits')
        else:
            return phone_number



class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'


    @validates('title')
    def validate_title(self, key, title):
        if title in title:
            raise ValueError(f'Title {title} already exists')
        elif title == '':
            raise ValueError(f'Title cannot be empty')
        else:
            return title
        
    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError(f'Content must be at least 250 characters')
        else:
            return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError(f'Summary must be less than 250 characters')
        else:
            return summary
        
    @validates('category')
    def validate_category(self, key, category):
        if category == '':
            raise ValueError(f'Category cannot be empty')
        elif category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError(f'Category must be Fiction or Non-Fiction')
        else:
            return category