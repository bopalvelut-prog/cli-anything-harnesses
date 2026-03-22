from setuptools import setup
setup(
    name='cli-anything-perpetual',
    version='1.0.0',
    packages=['cli_anything.perpetual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perpetual=cli_anything.perpetual:cli']},
)
