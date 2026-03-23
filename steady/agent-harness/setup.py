from setuptools import setup
setup(
    name='cli-anything-steady',
    version='1.0.0',
    packages=['cli_anything.steady'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-steady=cli_anything.steady:cli']},
)
