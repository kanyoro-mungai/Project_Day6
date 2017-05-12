from setuptools import setup

setup(
    
name = 'CalendarCli',
version = '1.0',
py_modules = ['calendarevent'],
install_requires = [

'Click',

],
entry_points = '''

    [console_scripts]
    AddEvent = calendarevent:cli
   

    '''
)
      
