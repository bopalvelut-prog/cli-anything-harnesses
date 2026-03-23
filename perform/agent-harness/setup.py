from setuptools import setup
setup(
    name='cli-anything-perform',
    version='1.0.0',
    packages=['cli_anything.perform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perform=cli_anything.perform:cli']},
)
