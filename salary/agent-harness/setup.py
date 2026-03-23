from setuptools import setup
setup(
    name='cli-anything-salary',
    version='1.0.0',
    packages=['cli_anything.salary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-salary=cli_anything.salary:cli']},
)
