from setuptools import setup
setup(
    name='cli-anything-relationship',
    version='1.0.0',
    packages=['cli_anything.relationship'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relationship=cli_anything.relationship:cli']},
)
