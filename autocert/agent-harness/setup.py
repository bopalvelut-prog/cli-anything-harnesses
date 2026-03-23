from setuptools import setup
setup(
    name='cli-anything-autocert',
    version='1.0.0',
    packages=['cli_anything.autocert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autocert=cli_anything.autocert:cli']},
)
