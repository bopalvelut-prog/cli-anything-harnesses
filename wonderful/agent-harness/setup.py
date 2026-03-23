from setuptools import setup
setup(
    name='cli-anything-wonderful',
    version='1.0.0',
    packages=['cli_anything.wonderful'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wonderful=cli_anything.wonderful:cli']},
)
