from setuptools import setup
setup(
    name='cli-anything-rely',
    version='1.0.0',
    packages=['cli_anything.rely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rely=cli_anything.rely:cli']},
)
