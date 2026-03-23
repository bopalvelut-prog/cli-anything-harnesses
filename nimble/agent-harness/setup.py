from setuptools import setup
setup(
    name='cli-anything-nimble',
    version='1.0.0',
    packages=['cli_anything.nimble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nimble=cli_anything.nimble:cli']},
)
