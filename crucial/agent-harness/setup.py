from setuptools import setup
setup(
    name='cli-anything-crucial',
    version='1.0.0',
    packages=['cli_anything.crucial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crucial=cli_anything.crucial:cli']},
)
