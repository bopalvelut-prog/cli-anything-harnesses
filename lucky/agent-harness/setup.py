from setuptools import setup
setup(
    name='cli-anything-lucky',
    version='1.0.0',
    packages=['cli_anything.lucky'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lucky=cli_anything.lucky:cli']},
)
