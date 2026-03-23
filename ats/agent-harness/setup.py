from setuptools import setup
setup(
    name='cli-anything-ats',
    version='1.0.0',
    packages=['cli_anything.ats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ats=cli_anything.ats:cli']},
)
