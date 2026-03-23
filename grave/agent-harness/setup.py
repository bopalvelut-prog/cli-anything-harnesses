from setuptools import setup
setup(
    name='cli-anything-grave',
    version='1.0.0',
    packages=['cli_anything.grave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grave=cli_anything.grave:cli']},
)
