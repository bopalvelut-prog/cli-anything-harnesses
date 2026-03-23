from setuptools import setup
setup(
    name='cli-anything-comanche',
    version='1.0.0',
    packages=['cli_anything.comanche'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-comanche=cli_anything.comanche:cli']},
)
