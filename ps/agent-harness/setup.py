from setuptools import setup
setup(
    name='cli-anything-ps',
    version='1.0.0',
    packages=['cli_anything.ps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ps=cli_anything.ps:cli']},
)
