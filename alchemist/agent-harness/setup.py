from setuptools import setup
setup(
    name='cli-anything-alchemist',
    version='1.0.0',
    packages=['cli_anything.alchemist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alchemist=cli_anything.alchemist:cli']},
)
