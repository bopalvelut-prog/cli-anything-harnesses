from setuptools import setup
setup(
    name='cli-anything-home',
    version='1.0.0',
    packages=['cli_anything.home'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-home=cli_anything.home:cli']},
)
