from setuptools import setup
setup(
    name='cli-anything-flat',
    version='1.0.0',
    packages=['cli_anything.flat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flat=cli_anything.flat:cli']},
)
