from setuptools import setup
setup(
    name='cli-anything-otherwise',
    version='1.0.0',
    packages=['cli_anything.otherwise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-otherwise=cli_anything.otherwise:cli']},
)
