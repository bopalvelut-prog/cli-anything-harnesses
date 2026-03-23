from setuptools import setup
setup(
    name='cli-anything-tableau',
    version='1.0.0',
    packages=['cli_anything.tableau'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tableau=cli_anything.tableau:cli']},
)
