from setuptools import setup
setup(
    name='cli-anything-stunnel',
    version='1.0.0',
    packages=['cli_anything.stunnel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stunnel=cli_anything.stunnel:cli']},
)
