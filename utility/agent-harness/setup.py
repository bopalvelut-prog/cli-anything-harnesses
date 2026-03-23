from setuptools import setup
setup(
    name='cli-anything-utility',
    version='1.0.0',
    packages=['cli_anything.utility'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-utility=cli_anything.utility:cli']},
)
