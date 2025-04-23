from rwydef.extensions import db
from sqlalchemy.exc import SQLAlchemyError
import datetime

class BaseMixin:
      id = db.Column(db.Integer(), primary_key=True)
      created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
      updated_at = db.Column(
            db.DateTime(),
            nullable=False,
            server_default=db.func.now(),
            onupdate=db.func.now(),
      )
      def save(self):
            try:
                  db.session.add(self)
                  db.session.commit()
            except SQLAlchemyError as e:
                  print(e)
                  db.session.rollback()

      def delete(self):    
            try:
                  db.session.delete(self)
                  db.session.commit()
            except Exception as e:
                  print(e)
                  db.session.rollback()      
      

class Donation(BaseMixin, db.Model):
      __tablename__ = "donations"
      __table_args__ = (
      db.CheckConstraint('amount > 0', name='positive_amount'),  # Reject negative values
      db.Index('idx_email', 'email'),  # for Faster email lookups
      )      
      firstname = db.Column(db.String(100),nullable=False)
      lastname = db.Column(db.String(100),nullable=False)
      email = db.Column(db.String(80))
      phone_no = db.Column(db.String(20))
      amount = db.Column(db.Numeric(10,2), nullable=False)