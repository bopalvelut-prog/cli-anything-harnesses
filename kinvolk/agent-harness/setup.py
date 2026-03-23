from setuptools import setup
setup(
    name='cli-anything-kinvolk',
    version='1.0.0',
    packages=['cli_anything.kinvolk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kinvolk=cli_anything.kinvolk:cli']},
)
