from setuptools import setup
setup(
    name='cli-anything-physician',
    version='1.0.0',
    packages=['cli_anything.physician'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-physician=cli_anything.physician:cli']},
)
