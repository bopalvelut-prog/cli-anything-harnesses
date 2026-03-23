from setuptools import setup
setup(
    name='cli-anything-eleven',
    version='1.0.0',
    packages=['cli_anything.eleven'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eleven=cli_anything.eleven:cli']},
)
