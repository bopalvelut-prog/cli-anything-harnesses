from setuptools import setup
setup(
    name='cli-anything-bitrise',
    version='1.0.0',
    packages=['cli_anything.bitrise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitrise=cli_anything.bitrise:cli']},
)
