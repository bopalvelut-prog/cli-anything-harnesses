from setuptools import setup
setup(
    name='cli-anything-deepblue',
    version='1.0.0',
    packages=['cli_anything.deepblue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deepblue=cli_anything.deepblue:cli']},
)
