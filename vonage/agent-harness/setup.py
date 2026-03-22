from setuptools import setup
setup(
    name='cli-anything-vonage',
    version='1.0.0',
    packages=['cli_anything.vonage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vonage=cli_anything.vonage:cli']},
)
