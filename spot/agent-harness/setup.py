from setuptools import setup
setup(
    name='cli-anything-spot',
    version='1.0.0',
    packages=['cli_anything.spot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spot=cli_anything.spot:cli']},
)
