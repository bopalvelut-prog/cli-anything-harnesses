from setuptools import setup
setup(
    name='cli-anything-unable',
    version='1.0.0',
    packages=['cli_anything.unable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unable=cli_anything.unable:cli']},
)
