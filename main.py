from pyscript import display, document

def grade_calculator(e):
    document.getElementById('output').innerHTML = ""

    # gets full name of student
    fname = document.getElementById('firstName').value
    lname = document.getElementById('lastName').value
    name = f'{fname} {lname}'

    display(f'Student Name: {name}', target='output')

    # all subject variables
    sci = int(document.getElementById('s1').value)
    eng = int(document.getElementById('s2').value)
    fil = int(document.getElementById('s3').value)
    math = int(document.getElementById('s4').value)
    ss = int(document.getElementById('s5').value)
    tle = int(document.getElementById('s6').value)

    # displays subject scores
    display(f'Science: {sci}', target='output')
    display(f'English: {eng}', target='output')
    display(f'Filipino: {fil}', target='output')
    display(f'Mathematics: {math}', target='output')
    display(f'Philosophy: {ss}', target='output')
    display(f'TLE: {tle}', target='output')

    subjects = [sci, eng, fil, math, ss, tle] # all subjecrs
    units = (5, 3, 2) # number of hours per subject

    # average weighted score
    final = int(((subjects[0] * units[0]) + (subjects[1] * units[0]) + (subjects[2] * units[1]) + (subjects[3] * units[0]) + (subjects[4] * units[1]) + (subjects[5] * units[2])) / (units[0] + units[0] + units[1] + units[0] + units[1] + units[2]))

    if final > 70:
        display(f'Weighted Average: {final}', target='output')
        display(f'You passed.', target='output')
    else:
        display(f'Weighted Average: {final}', target='output')
        display(f'You failed.', target='output')


