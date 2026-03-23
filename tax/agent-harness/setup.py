from setuptools import setup
setup(
    name='cli-anything-tax',
    version='1.0.0',
    packages=['cli_anything.tax'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tax=cli_anything.tax:cli']},
)
