from setuptools import setup
setup(
    name='cli-anything-sale',
    version='1.0.0',
    packages=['cli_anything.sale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sale=cli_anything.sale:cli']},
)
