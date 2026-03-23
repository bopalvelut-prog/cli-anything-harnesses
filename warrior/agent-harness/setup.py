from setuptools import setup
setup(
    name='cli-anything-warrior',
    version='1.0.0',
    packages=['cli_anything.warrior'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warrior=cli_anything.warrior:cli']},
)
