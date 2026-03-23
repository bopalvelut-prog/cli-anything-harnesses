from setuptools import setup
setup(
    name='cli-anything-royal',
    version='1.0.0',
    packages=['cli_anything.royal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-royal=cli_anything.royal:cli']},
)
