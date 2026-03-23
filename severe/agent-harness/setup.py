from setuptools import setup
setup(
    name='cli-anything-severe',
    version='1.0.0',
    packages=['cli_anything.severe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-severe=cli_anything.severe:cli']},
)
