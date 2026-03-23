from setuptools import setup
setup(
    name='cli-anything-key',
    version='1.0.0',
    packages=['cli_anything.key'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-key=cli_anything.key:cli']},
)
