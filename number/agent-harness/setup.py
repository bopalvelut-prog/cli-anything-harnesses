from setuptools import setup
setup(
    name='cli-anything-number',
    version='1.0.0',
    packages=['cli_anything.number'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-number=cli_anything.number:cli']},
)
