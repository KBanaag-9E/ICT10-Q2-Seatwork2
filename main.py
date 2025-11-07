from pyscript import display, document

def grade_calculator(e):
    document.getElementById('output').innerHTML = ""

    # gets full name of student
    fname = document.getElementById('firstName').value
    lname = document.getElementById('lastName').value
    name = f'{fname} {lname}'

    display(f'Student Name: {name}', target='output')

    # all subject variables
    sci = document.getElementById('s1').value
    eng = document.getElementById('s2').value
    fil = document.getElementById('s3').value
    math = document.getElementById('s4').value
    ss = document.getElementById('s5').value
    tle = document.getElementById('s6').value

    # displays subject scores
    display(f'Science: {sci}', target='output')
    display(f'English: {eng}', target='output')
    display(f'Filipino: {fil}', target='output')
    display(f'Mathematics: {math}', target='output')
    display(f'Philosophy: {ss}', target='output')
    display(f'TLE: {tle}', target='output')

    # assigns the default value of the subject input as 0 if no input is detected
    sci = int(("") or 0)
    eng = int(("") or 0)
    fil = int(("") or 0)
    math = int(("") or 0)
    ss = int(("") or 0)
    tle = int(("") or 0)

    subjects = [sci, eng, fil, math, ss, tle] # all subjecrs
    units = (5, 3, 2) # number of hours per subject

    # average weighted score
    final = round((float(subjects[0]) * units[0] +
        float(subjects[1]) * units[0] +
        float(subjects[2]) * units[1] +
        float(subjects[3]) * units[0] +
        float(subjects[4]) * units[1] +
        float(subjects[5]) * units[2]) / 
        (units[0] + units[0] + units[1] + units[0] + units[1] + units[2]), 2)

    display(f'Weighted Average: {final}', target='output')