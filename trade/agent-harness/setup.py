from setuptools import setup
setup(
    name='cli-anything-trade',
    version='1.0.0',
    packages=['cli_anything.trade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trade=cli_anything.trade:cli']},
)
