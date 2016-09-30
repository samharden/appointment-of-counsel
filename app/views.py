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
  first_name = session['first_name']
  last_name = session['last_name']
  l_n_f_l = last_name[:1]


  print state
  print judge
  print charge
  print first_name
  print last_name
  print l_n_f_l

  ###########   LOGIC ROUTING ################################


  ###### DUI #################
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

####### BATTERY ################

  elif state == 'fl' and county == 'hill' and judge == 'farr' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('farrbat'))
  
  elif state == 'fl' and county == 'hill' and judge == 'greco' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('grecobat'))

  elif state == 'fl' and county == 'hill' and judge == 'jeske' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('jeskebat'))

  elif state == 'fl' and county == 'hill' and judge == 'lefler' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('leflerbat'))

  elif state == 'fl' and county == 'hill' and judge == 'mcneil' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('mcneilbat'))

  elif state == 'fl' and county == 'hill' and judge == 'myers' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('myersbat'))

  elif state == 'fl' and county == 'hill' and judge == 'taylor' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('taylorbat'))

  elif state == 'fl' and county == 'hill' and judge == 'none' and charge == 'bat' and agree == True and form.validate_on_submit():
    return redirect(url_for('hillbat'))

######## DWLSR ######################

  elif state == 'fl' and county == 'hill' and judge == 'farr' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('farrdwlsr'))
  
  elif state == 'fl' and county == 'hill' and judge == 'greco' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('grecodwlsr'))

  elif state == 'fl' and county == 'hill' and judge == 'jeske' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('jeskedwlsr'))

  elif state == 'fl' and county == 'hill' and judge == 'lefler' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('leflerdwlsr'))

  elif state == 'fl' and county == 'hill' and judge == 'mcneil' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('mcneildwlsr'))

  elif state == 'fl' and county == 'hill' and judge == 'myers' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('myersdwlsr'))

  elif state == 'fl' and county == 'hill' and judge == 'taylor' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('taylordwlsr'))

  elif state == 'fl' and county == 'hill' and judge == 'none' and charge == 'dwls' and agree == True and form.validate_on_submit():
    return redirect(url_for('hilldwlsr'))


######## PETIT THEFT ######################

  elif state == 'fl' and county == 'hill' and judge == 'farr' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('farrpetittheft'))
  
  elif state == 'fl' and county == 'hill' and judge == 'greco' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('grecopetittheft'))

  elif state == 'fl' and county == 'hill' and judge == 'jeske' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('jeskepetittheft'))

  elif state == 'fl' and county == 'hill' and judge == 'lefler' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('leflerpetittheft'))

  elif state == 'fl' and county == 'hill' and judge == 'mcneil' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('mcneilpetittheft'))

  elif state == 'fl' and county == 'hill' and judge == 'myers' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('myerspetittheft'))

  elif state == 'fl' and county == 'hill' and judge == 'taylor' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('taylorpetittheft'))

  elif state == 'fl' and county == 'hill' and judge == 'none' and charge == 'petit_theft' and agree == True and form.validate_on_submit():
    return redirect(url_for('hillpetittheft'))



######### END ###################

  elif state == 'fl':
    flash(try_again)


  return render_template('homepage.html',
                           title='My Court Case',
                           form=form)


#######   DUI    ##########################


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

#######   BATTERY   #########

@app.route('/fl/hillsborough/battery/battery.html', methods=['GET', 'POST'])
def hillbat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/battery.html',
                           title='Hillsborough County Battery Cases')

@app.route('/fl/hillsborough/battery/farrbattery.html', methods=['GET', 'POST'])
def farrbat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/farrbattery.html',
                           title='Hillsborough County Judge Farr Battery Cases')


@app.route('/fl/hillsborough/battery/grecobattery.html', methods=['GET', 'POST'])
def grecobat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/grecobattery.html',
                           title='Hillsborough County Judge Greco Battery Cases')


@app.route('/fl/hillsborough/battery/jeskebattery.html', methods=['GET', 'POST'])
def jeskebat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/jeskebattery.html',
                           title='Hillsborough County Judge Jeske Battery Cases')


@app.route('/fl/hillsborough/battery/leflerbattery.html', methods=['GET', 'POST'])
def leflerbat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/leflerbattery.html',
                           title='Hillsborough County Judge Lefler Battery Cases')


@app.route('/fl/hillsborough/battery/mcneilbattery.html', methods=['GET', 'POST'])
def mcneilbat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/mcneilbattery.html',
                           title='Hillsborough County Judge McNeil Battery Cases')


@app.route('/fl/hillsborough/battery/myersbattery.html', methods=['GET', 'POST'])
def myersbat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/myersbattery.html',
                           title='Hillsborough County Judge Myers Battery Cases')


@app.route('/fl/hillsborough/battery/taylorbattery.html', methods=['GET', 'POST'])
def taylorbat():
  print "Top of index"
  return render_template('fl/hillsborough/battery/taylorbattery.html',
                           title='Hillsborough County Judge Taylor Battery Cases')


#######   DWLSR  #########

@app.route('/fl/hillsborough/dwlsr/dwlsr.html', methods=['GET', 'POST'])
def hilldwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/dwlsr.html',
                           title='Hillsborough County DWLSR Cases')

@app.route('/fl/hillsborough/dwlsr/farrdwlsr.html', methods=['GET', 'POST'])
def farrdwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/farrdwlsr.html',
                           title='Hillsborough County Judge Farr DWLSR Cases')


@app.route('/fl/hillsborough/dwlsr/grecodwlsr.html', methods=['GET', 'POST'])
def grecodwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/grecodwlsr.html',
                           title='Hillsborough County Judge Greco DWLSR Cases')


@app.route('/fl/hillsborough/dwlsr/jeskedwlsr.html', methods=['GET', 'POST'])
def jeskedwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/jeskedwlsr.html',
                           title='Hillsborough County Judge Jeske DWLSR Cases')


@app.route('/fl/hillsborough/dwlsr/leflerdwlsr.html', methods=['GET', 'POST'])
def leflerdwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/leflerdwlsr.html',
                           title='Hillsborough County Judge Lefler DWLSR Cases')


@app.route('/fl/hillsborough/dwlsr/mcneildwlsr.html', methods=['GET', 'POST'])
def mcneildwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/mcneildwlsr.html',
                           title='Hillsborough County Judge McNeil DWLSR Cases')


@app.route('/fl/hillsborough/dwlsr/myersdwlsr.html', methods=['GET', 'POST'])
def myersdwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/myersdwlsr.html',
                           title='Hillsborough County Judge Myers DWLSR Cases')


@app.route('/fl/hillsborough/dwlsr/taylordwlsr.html', methods=['GET', 'POST'])
def taylordwlsr():
  print "Top of index"
  return render_template('fl/hillsborough/dwlsr/taylordwlsr.html',
                           title='Hillsborough County Judge Taylor DWLSR Cases')


#######   Petit Theft    ##########################


@app.route('/fl/hillsborough/petit-theft/farrpetittheft.html', methods=['GET', 'POST'])
def farrpetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/farrpetittheft.html',
                           title='Judge Farr Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/greopetittheft.html', methods=['GET', 'POST'])
def grecopetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/grecopetittheft.html',
                           title='Judge Greco Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/jeskepetittheft.html', methods=['GET', 'POST'])
def jeskepetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/jeskepetittheft.html',
                           title='Judge Jeske Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/leflerpetittheft.html', methods=['GET', 'POST'])
def leflerpetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/leflerpetittheft.html',
                           title='Judge Lefler Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/mcneilpetittheft.html', methods=['GET', 'POST'])
def mcneilpetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/mcneilpetittheft.html',
                           title='Judge McNeil Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/myerspetittheft.html', methods=['GET', 'POST'])
def myerspetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/myerspetittheft.html',
                           title='Judge Myers Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/taylorpetittheft.html', methods=['GET', 'POST'])
def taylorpetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/taylorpetittheft.html',
                           title='Judge Taylor Petit Theft Cases')

@app.route('/fl/hillsborough/petit-theft/petittheft.html', methods=['GET', 'POST'])
def hillpetittheft():
  print "Top of index"
  return render_template('fl/hillsborough/petit-theft/petittheft.html',
                           title='Hillsborough County Petit Theft Cases')

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