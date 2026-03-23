from setuptools import setup
setup(
    name='cli-anything-product',
    version='1.0.0',
    packages=['cli_anything.product'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-product=cli_anything.product:cli']},
)
