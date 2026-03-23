from setuptools import setup
setup(
    name='cli-anything-bullet',
    version='1.0.0',
    packages=['cli_anything.bullet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bullet=cli_anything.bullet:cli']},
)
