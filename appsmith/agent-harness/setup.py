from setuptools import setup
setup(
    name='cli-anything-appsmith',
    version='1.0.0',
    packages=['cli_anything.appsmith'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appsmith=cli_anything.appsmith:cli']},
)
