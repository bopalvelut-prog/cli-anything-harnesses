from setuptools import setup
setup(
    name='cli-anything-gatus',
    version='1.0.0',
    packages=['cli_anything.gatus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gatus=cli_anything.gatus:cli']},
)
