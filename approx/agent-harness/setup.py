from setuptools import setup
setup(
    name='cli-anything-approx',
    version='1.0.0',
    packages=['cli_anything.approx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-approx=cli_anything.approx:cli']},
)
