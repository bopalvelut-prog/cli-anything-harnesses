from setuptools import setup
setup(
    name='cli-anything-scan',
    version='1.0.0',
    packages=['cli_anything.scan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scan=cli_anything.scan:cli']},
)
