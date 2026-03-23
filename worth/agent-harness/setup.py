from setuptools import setup
setup(
    name='cli-anything-worth',
    version='1.0.0',
    packages=['cli_anything.worth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-worth=cli_anything.worth:cli']},
)
