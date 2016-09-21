from flask import render_template, flash, redirect, url_for, session, Markup, request, g
from app import app
from .forms import s_c_j_c




print "Top of Views"
@app.route('/', methods=['GET', 'POST'])

@app.route('/homepage', methods=['GET', 'POST'])
def index():
  try_again = Markup("""<h3 style=""><center>You must complete all fields""")
  form = s_c_j_c()
  session['state'] = form.state.data
  session['county'] = form.county.data
  session['judge'] = form.judge.data
  session['charge'] = form.charge.data
  session['first_name'] = form.first_name._value()
  session['last_name'] = form.last_name._value()
  session['agree'] = form.agree.data

  state = session['state']
  county = session['county']
  judge = session['judge']
  charge = session['charge']
  agree = session['agree']

  print state
  print judge


  #small claims complaint
  if state == 'fl' and county == 'hill' and judge == 'farr' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('farrdui'))
  
  elif state == 'fl' and county == 'hill' and judge == 'greco' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('grecodui'))

  elif state == 'fl' and county == 'hill' and judge == 'jeske' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('jeskedui'))

  elif state == 'fl' and county == 'hill' and judge == 'lefler' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('leflerdui'))

  elif state == 'fl' and county == 'hill' and judge == 'mcneil' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('mcneildui'))

  elif state == 'fl' and county == 'hill' and judge == 'myers' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('myersdui'))

  elif state == 'fl' and county == 'hill' and judge == 'taylor' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('taylordui'))

  elif state == 'fl' and county == 'hill' and judge == 'none' and charge == 'dui' and agree == True and form.validate_on_submit():
    return redirect(url_for('hilldui'))

  elif state == 'fl':
    flash(try_again)


  return render_template('homepage.html',
                           title='My Court Case',
                           form=form)


@app.route('/fl/hillsborough/dui/farrdui.html', methods=['GET', 'POST'])
def farrdui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/farrdui.html',
                           title='Judge Farr DUI Cases')

@app.route('/fl/hillsborough/dui/grecodui.html', methods=['GET', 'POST'])
def grecodui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/grecodui.html',
                           title='Judge Greco DUI Cases')

@app.route('/fl/hillsborough/dui/jeskedui.html', methods=['GET', 'POST'])
def jeskedui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/jeskedui.html',
                           title='Judge Jeske DUI Cases')


@app.route('/fl/hillsborough/dui/leflerdui.html', methods=['GET', 'POST'])
def leflerdui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/leflerdui.html',
                           title='Judge Lefler DUI Cases')


@app.route('/fl/hillsborough/dui/mcneildui.html', methods=['GET', 'POST'])
def mcneildui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/mcneildui.html',
                           title='Judge McNeil DUI Cases')


@app.route('/fl/hillsborough/dui/myersdui.html', methods=['GET', 'POST'])
def myersdui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/myersdui.html',
                           title='Judge Myers DUI Cases')


@app.route('/fl/hillsborough/dui/taylordui.html', methods=['GET', 'POST'])
def taylordui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/taylordui.html',
                           title='Judge Taylor DUI Cases')


@app.route('/fl/hillsborough/dui/dui.html', methods=['GET', 'POST'])
def hilldui():
  print "Top of index"
  return render_template('fl/hillsborough/dui/dui.html',
                           title='Hillsborough County DUI Cases')

#Error Handling:
    
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-unit-testing
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500
    

@app.route('/style.css')
def style():
  return render_template('style.css',
                           title='Style Sheet')