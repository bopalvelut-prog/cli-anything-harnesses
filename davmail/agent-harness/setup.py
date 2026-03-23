from setuptools import setup
setup(
    name='cli-anything-davmail',
    version='1.0.0',
    packages=['cli_anything.davmail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-davmail=cli_anything.davmail:cli']},
)
