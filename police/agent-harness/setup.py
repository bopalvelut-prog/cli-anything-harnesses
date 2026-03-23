from setuptools import setup
setup(
    name='cli-anything-police',
    version='1.0.0',
    packages=['cli_anything.police'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-police=cli_anything.police:cli']},
)
