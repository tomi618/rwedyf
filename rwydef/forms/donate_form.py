from wtforms.validators import DataRequired, Length, Email, ValidationError, NumberRange
from wtforms import StringField, SubmitField, TextAreaField, DecimalField
from flask_wtf import FlaskForm 

class DonationForm(FlaskForm):
      firstname = StringField("First Name", validators=[DataRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Aminat"})
      lastname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Ozovehe"})
      phone_no = StringField("Phone Number", validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "08012345678"})
      email = StringField("Email", render_kw={"placeholder": "you@example.com"}) #, validators=[Email()])
      amount = DecimalField(
        "Amount (Naira)", 
        validators=[
            DataRequired(message="Please enter an amount"),
            NumberRange(min=100, message="Amount must be positive")
        ],
        render_kw={"min": "100", "step": "100"},
        places=2  # Ensures 2 decimal places (e.g., 10.50)
    )
      submit = SubmitField("Donate")
      