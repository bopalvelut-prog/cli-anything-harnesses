from setuptools import setup
setup(
    name='cli-anything-scanner',
    version='1.0.0',
    packages=['cli_anything.scanner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scanner=cli_anything.scanner:cli']},
)
