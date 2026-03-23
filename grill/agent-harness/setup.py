from setuptools import setup
setup(
    name='cli-anything-grill',
    version='1.0.0',
    packages=['cli_anything.grill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grill=cli_anything.grill:cli']},
)
