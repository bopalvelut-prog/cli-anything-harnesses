from setuptools import setup
setup(
    name='cli-anything-taco',
    version='1.0.0',
    packages=['cli_anything.taco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-taco=cli_anything.taco:cli']},
)
