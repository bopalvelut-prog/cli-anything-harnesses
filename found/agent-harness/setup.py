from setuptools import setup
setup(
    name='cli-anything-found',
    version='1.0.0',
    packages=['cli_anything.found'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-found=cli_anything.found:cli']},
)
