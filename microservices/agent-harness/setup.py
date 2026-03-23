from setuptools import setup
setup(
    name='cli-anything-microservices',
    version='1.0.0',
    packages=['cli_anything.microservices'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-microservices=cli_anything.microservices:cli']},
)
