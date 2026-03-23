from setuptools import setup
setup(
    name='cli-anything-income',
    version='1.0.0',
    packages=['cli_anything.income'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-income=cli_anything.income:cli']},
)
