from setuptools import setup
setup(
    name='cli-anything-amazon_frauddetector',
    version='1.0.0',
    packages=['cli_anything.amazon_frauddetector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_frauddetector=cli_anything.amazon_frauddetector:cli']},
)
