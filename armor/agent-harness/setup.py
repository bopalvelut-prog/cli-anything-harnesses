from setuptools import setup
setup(
    name='cli-anything-armor',
    version='1.0.0',
    packages=['cli_anything.armor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-armor=cli_anything.armor:cli']},
)
