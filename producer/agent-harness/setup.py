from setuptools import setup
setup(
    name='cli-anything-producer',
    version='1.0.0',
    packages=['cli_anything.producer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-producer=cli_anything.producer:cli']},
)
