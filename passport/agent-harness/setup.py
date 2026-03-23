from setuptools import setup
setup(
    name='cli-anything-passport',
    version='1.0.0',
    packages=['cli_anything.passport'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-passport=cli_anything.passport:cli']},
)
