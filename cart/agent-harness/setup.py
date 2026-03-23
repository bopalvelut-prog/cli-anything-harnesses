from setuptools import setup
setup(
    name='cli-anything-cart',
    version='1.0.0',
    packages=['cli_anything.cart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cart=cli_anything.cart:cli']},
)
