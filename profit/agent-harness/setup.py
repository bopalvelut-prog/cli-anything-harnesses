from setuptools import setup
setup(
    name='cli-anything-profit',
    version='1.0.0',
    packages=['cli_anything.profit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-profit=cli_anything.profit:cli']},
)
