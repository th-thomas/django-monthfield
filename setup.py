'''Still needs some work to properly include the test_site and sqlite db'''

from setuptools import setup

setup(
    name='django-monthfield-custom',
    version='0.1.3',
    author=u'Thibault THOMAS',
    author_email='thibaulthomas@gmail.com',
    packages=['month'],
    include_package_data=True,
    url='https://github.com/th-thomas/django-monthfield',
    license='BSD licence, see LICENCE',
    description='Provides a field for storing months (YYYY-MM) on django models.',
    long_description=open('README.rst').read(),
    zip_safe=False,
)
