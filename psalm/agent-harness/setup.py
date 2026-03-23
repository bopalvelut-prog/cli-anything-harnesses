from setuptools import setup
setup(
    name='cli-anything-psalm',
    version='1.0.0',
    packages=['cli_anything.psalm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-psalm=cli_anything.psalm:cli']},
)
