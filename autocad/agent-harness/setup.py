from setuptools import setup
setup(
    name='cli-anything-autocad',
    version='1.0.0',
    packages=['cli_anything.autocad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autocad=cli_anything.autocad:cli']},
)
