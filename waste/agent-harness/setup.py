from setuptools import setup
setup(
    name='cli-anything-waste',
    version='1.0.0',
    packages=['cli_anything.waste'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-waste=cli_anything.waste:cli']},
)
