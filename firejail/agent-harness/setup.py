from setuptools import setup
setup(
    name='cli-anything-firejail',
    version='1.0.0',
    packages=['cli_anything.firejail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firejail=cli_anything.firejail:cli']},
)
