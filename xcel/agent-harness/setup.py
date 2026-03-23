from setuptools import setup
setup(
    name='cli-anything-xcel',
    version='1.0.0',
    packages=['cli_anything.xcel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xcel=cli_anything.xcel:cli']},
)
