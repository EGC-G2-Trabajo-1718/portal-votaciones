from setuptools import setup
from setuptools import find_packages

setup(
    name='visualizacion_resultados',
    version='3.1',
    description='Contiene las utilidades necesarias para la visualizacion de resultados del sistema de votaciones de EGC 17/18',
    url='https://github.com/EGC-G2-Trabajo-1718/portal-votaciones',
    author='grupo visualizacion de resultados idopera83',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask',
    'Flask-Login',
    'Flask-Babel',
    'Flask-Principal',
    'Flask-Via',
    'Flask-WTF',
    'Jinja2',
    'MarkupSafe',
    'Werkzeug',
    'click',
    'itsdangerous',
    'requests']
)
