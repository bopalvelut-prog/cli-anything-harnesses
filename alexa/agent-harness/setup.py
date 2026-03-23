from setuptools import setup
setup(
    name='cli-anything-alexa',
    version='1.0.0',
    packages=['cli_anything.alexa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alexa=cli_anything.alexa:cli']},
)
