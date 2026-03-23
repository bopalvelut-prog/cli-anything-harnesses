from setuptools import setup
setup(
    name='cli-anything-paragon',
    version='1.0.0',
    packages=['cli_anything.paragon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paragon=cli_anything.paragon:cli']},
)
