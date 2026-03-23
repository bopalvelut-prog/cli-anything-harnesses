from setuptools import setup
setup(
    name='cli-anything-prince',
    version='1.0.0',
    packages=['cli_anything.prince'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prince=cli_anything.prince:cli']},
)
