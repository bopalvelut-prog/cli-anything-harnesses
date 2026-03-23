from setuptools import setup
setup(
    name='cli-anything-pray',
    version='1.0.0',
    packages=['cli_anything.pray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pray=cli_anything.pray:cli']},
)
