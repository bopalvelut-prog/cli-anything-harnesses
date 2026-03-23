from setuptools import setup
setup(
    name='cli-anything-amazon_comprehend',
    version='1.0.0',
    packages=['cli_anything.amazon_comprehend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_comprehend=cli_anything.amazon_comprehend:cli']},
)
