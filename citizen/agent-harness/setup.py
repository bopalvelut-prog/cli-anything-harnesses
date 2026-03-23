from setuptools import setup
setup(
    name='cli-anything-citizen',
    version='1.0.0',
    packages=['cli_anything.citizen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-citizen=cli_anything.citizen:cli']},
)
