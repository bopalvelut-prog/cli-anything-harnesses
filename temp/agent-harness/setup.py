from setuptools import setup
setup(
    name='cli-anything-temp',
    version='1.0.0',
    packages=['cli_anything.temp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-temp=cli_anything.temp:cli']},
)
