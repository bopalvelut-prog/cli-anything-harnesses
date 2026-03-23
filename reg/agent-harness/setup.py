from setuptools import setup
setup(
    name='cli-anything-reg',
    version='1.0.0',
    packages=['cli_anything.reg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reg=cli_anything.reg:cli']},
)
