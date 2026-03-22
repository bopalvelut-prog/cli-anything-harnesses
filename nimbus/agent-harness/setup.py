from setuptools import setup
setup(
    name='cli-anything-nimbus',
    version='1.0.0',
    packages=['cli_anything.nimbus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nimbus=cli_anything.nimbus:cli']},
)
