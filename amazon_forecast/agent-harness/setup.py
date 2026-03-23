from setuptools import setup
setup(
    name='cli-anything-amazon_forecast',
    version='1.0.0',
    packages=['cli_anything.amazon_forecast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_forecast=cli_anything.amazon_forecast:cli']},
)
