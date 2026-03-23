from setuptools import setup
setup(
    name='cli-anything-apache_dubbo',
    version='1.0.0',
    packages=['cli_anything.apache_dubbo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_dubbo=cli_anything.apache_dubbo:cli']},
)
