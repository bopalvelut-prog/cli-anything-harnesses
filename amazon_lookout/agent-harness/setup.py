from setuptools import setup
setup(
    name='cli-anything-amazon_lookout',
    version='1.0.0',
    packages=['cli_anything.amazon_lookout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_lookout=cli_anything.amazon_lookout:cli']},
)
