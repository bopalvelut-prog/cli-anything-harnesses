from setuptools import setup
setup(
    name='cli-anything-scamper',
    version='1.0.0',
    packages=['cli_anything.scamper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scamper=cli_anything.scamper:cli']},
)
