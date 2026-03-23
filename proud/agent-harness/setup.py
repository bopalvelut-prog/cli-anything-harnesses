from setuptools import setup
setup(
    name='cli-anything-proud',
    version='1.0.0',
    packages=['cli_anything.proud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proud=cli_anything.proud:cli']},
)
