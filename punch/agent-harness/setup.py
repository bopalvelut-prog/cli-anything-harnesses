from setuptools import setup
setup(
    name='cli-anything-punch',
    version='1.0.0',
    packages=['cli_anything.punch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-punch=cli_anything.punch:cli']},
)
