from distutils.core import setup

setup(
    name='Quine',
    version=open('CHANGES.txt').read().split()[0],
    author='BoppreH',
    author_email='contact@boppreh.com',
    packages=['quine'],
    url='http://pypi.python.org/pypi/Quine/',
    license='LICENSE.txt',
    description='Quine generator.',
    long_description=open('README.rst').read() + '\n\Last Updates\n-------------\n' + open('CHANGES.txt').read(),
)
