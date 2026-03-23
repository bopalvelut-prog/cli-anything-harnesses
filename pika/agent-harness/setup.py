from setuptools import setup
setup(
    name='cli-anything-pika',
    version='1.0.0',
    packages=['cli_anything.pika'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pika=cli_anything.pika:cli']},
)
