from flask import flash, Markup
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField, SelectField, RadioField, TextAreaField, validators
from wtforms.validators import DataRequired
#here is where you build your forms under the InputForm class:

class s_c_j_c(Form):
  
  state = SelectField('state', choices=[('fl','Florida')])
  county = SelectField('county', choices=[('hill','Hillsborough')])
  judge = SelectField('judge', choices=[('farr','Farr'), ('greco','Greco'), 
                                        ('jeske','Jeske'),('lefler','Lefler'), 
                                        ('mcneil','McNeil'),('myers','Myers'),
                                        ('taylor','Taylor'), ('none','Not Sure') ])
  charge = SelectField('charge', choices=[('dui','DUI'), ('bat','Battery'), 
                                          ('dwls', 'Driving While License Suspended'),
                                          ('mjposs', 'Marijuana Possession'),
                                          ('petit_theft', 'Petit Theft')])
  first_name = TextField('first_name')
  last_name = TextField('last_name')
  agree = BooleanField('agree')

  
