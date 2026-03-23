from setuptools import setup
setup(
    name='cli-anything-price',
    version='1.0.0',
    packages=['cli_anything.price'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-price=cli_anything.price:cli']},
)
