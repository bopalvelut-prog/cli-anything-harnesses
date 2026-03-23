from setuptools import setup
setup(
    name='cli-anything-arcjet',
    version='1.0.0',
    packages=['cli_anything.arcjet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arcjet=cli_anything.arcjet:cli']},
)
