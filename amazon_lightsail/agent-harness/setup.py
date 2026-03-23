from setuptools import setup
setup(
    name='cli-anything-amazon_lightsail',
    version='1.0.0',
    packages=['cli_anything.amazon_lightsail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_lightsail=cli_anything.amazon_lightsail:cli']},
)
