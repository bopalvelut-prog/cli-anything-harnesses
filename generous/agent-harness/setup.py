from setuptools import setup
setup(
    name='cli-anything-generous',
    version='1.0.0',
    packages=['cli_anything.generous'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-generous=cli_anything.generous:cli']},
)
