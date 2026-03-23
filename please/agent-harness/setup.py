from setuptools import setup
setup(
    name='cli-anything-please',
    version='1.0.0',
    packages=['cli_anything.please'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-please=cli_anything.please:cli']},
)
