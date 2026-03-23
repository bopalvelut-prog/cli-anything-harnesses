from setuptools import setup
setup(
    name='cli-anything-smile',
    version='1.0.0',
    packages=['cli_anything.smile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smile=cli_anything.smile:cli']},
)
