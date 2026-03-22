from setuptools import setup
setup(
    name='cli-anything-braco11',
    version='1.0.0',
    packages=['cli_anything.braco11'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco11=cli_anything.braco11:cli']},
)
