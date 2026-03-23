from setuptools import setup
setup(
    name='cli-anything-male',
    version='1.0.0',
    packages=['cli_anything.male'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-male=cli_anything.male:cli']},
)
