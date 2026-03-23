from setuptools import setup
setup(
    name='cli-anything-majority',
    version='1.0.0',
    packages=['cli_anything.majority'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-majority=cli_anything.majority:cli']},
)
