from setuptools import setup
setup(
    name='cli-anything-splice',
    version='1.0.0',
    packages=['cli_anything.splice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-splice=cli_anything.splice:cli']},
)
