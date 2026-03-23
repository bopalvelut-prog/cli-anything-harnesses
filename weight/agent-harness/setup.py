from setuptools import setup
setup(
    name='cli-anything-weight',
    version='1.0.0',
    packages=['cli_anything.weight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weight=cli_anything.weight:cli']},
)
