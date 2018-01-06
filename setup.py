from setuptools import setup

setup(
   name='encoding-python-assignment',
   version='1.0',
   packages=['src','tst'],
   description='python-assignment',
   author='Angelos Sakellaropoulos',
   author_email='angsakel@gmail.com',
   python_requires='==2.7',
   install_requires=['mock', 'requests'],
)
