from setuptools import setup
setup(
    name='cli-anything-canyon',
    version='1.0.0',
    packages=['cli_anything.canyon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-canyon=cli_anything.canyon:cli']},
)
