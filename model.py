from wtforms import Form, StringField, TextAreaField, FloatField, SubmitField, validators
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField
from math import pi

class InputForm(Form):
        Amplitude = FloatField(label='(m)', default = 1.0, validators=[validators.InputRequired()])
        Damping_Factor = FloatField(label='(kg/s)', default = 0, validators=[validators.InputRequired()])
        Frequency = FloatField(label='(1/s)', default = 2*pi, validators=[validators.InputRequired()])
        Time_Interval = FloatField(label='(s)', default = 18, validators=[validators.InputRequired()])
