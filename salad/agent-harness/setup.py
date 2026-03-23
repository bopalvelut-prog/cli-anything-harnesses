from setuptools import setup
setup(
    name='cli-anything-salad',
    version='1.0.0',
    packages=['cli_anything.salad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-salad=cli_anything.salad:cli']},
)
