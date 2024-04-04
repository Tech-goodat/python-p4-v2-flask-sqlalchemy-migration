from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata=MetaData()

db=SQLAlchemy(metadata=metadata)

class Employee(db.Model):
    __tablename__='employees'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    salary=db.Column(db.Integer)


    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.salary}>'
    
class Department(db.Model):
    __tablename__="department"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    address=db.Column(db.Integer)

    def __repr__(self):
        return f'<Detartment {self.id}, {self.name}, {self.address}'