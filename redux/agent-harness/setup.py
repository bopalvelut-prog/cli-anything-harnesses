from setuptools import setup
setup(
    name='cli-anything-redux',
    version='1.0.0',
    packages=['cli_anything.redux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redux=cli_anything.redux:cli']},
)
