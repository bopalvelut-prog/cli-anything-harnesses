from setuptools import setup
setup(
    name='cli-anything-integration',
    version='1.0.0',
    packages=['cli_anything.integration'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-integration=cli_anything.integration:cli']},
)
