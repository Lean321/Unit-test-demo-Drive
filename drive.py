
def fdrive(name,age,flag):
    vcondition = 'is' if age >= flag else 'not'
    return(f'{name} {vcondition} allowed to drive')
