from setuptools import setup
setup(
    name='cli-anything-solar',
    version='1.0.0',
    packages=['cli_anything.solar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solar=cli_anything.solar:cli']},
)
