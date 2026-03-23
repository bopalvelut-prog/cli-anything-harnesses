from setuptools import setup
setup(
    name='cli-anything-hall',
    version='1.0.0',
    packages=['cli_anything.hall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hall=cli_anything.hall:cli']},
)
