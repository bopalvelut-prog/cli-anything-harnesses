from setuptools import setup
setup(
    name='cli-anything-modern',
    version='1.0.0',
    packages=['cli_anything.modern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-modern=cli_anything.modern:cli']},
)
