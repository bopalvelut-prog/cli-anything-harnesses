from setuptools import setup
setup(
    name='cli-anything-ronin',
    version='1.0.0',
    packages=['cli_anything.ronin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ronin=cli_anything.ronin:cli']},
)
