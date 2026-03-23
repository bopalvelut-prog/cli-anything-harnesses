from setuptools import setup
setup(
    name='cli-anything-library',
    version='1.0.0',
    packages=['cli_anything.library'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-library=cli_anything.library:cli']},
)
