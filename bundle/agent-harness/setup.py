from setuptools import setup
setup(
    name='cli-anything-bundle',
    version='1.0.0',
    packages=['cli_anything.bundle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bundle=cli_anything.bundle:cli']},
)
