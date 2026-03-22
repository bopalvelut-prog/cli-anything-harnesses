from setuptools import setup
setup(
    name='cli-anything-teku',
    version='1.0.0',
    packages=['cli_anything.teku'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-teku=cli_anything.teku:cli']},
)
