from setuptools import setup
setup(
    name='cli-anything-saleor',
    version='1.0.0',
    packages=['cli_anything.saleor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-saleor=cli_anything.saleor:cli']},
)
