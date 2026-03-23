from setuptools import setup
setup(
    name='cli-anything-davinci',
    version='1.0.0',
    packages=['cli_anything.davinci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-davinci=cli_anything.davinci:cli']},
)
