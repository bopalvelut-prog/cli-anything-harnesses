from setuptools import setup
setup(
    name='cli-anything-volatile',
    version='1.0.0',
    packages=['cli_anything.volatile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-volatile=cli_anything.volatile:cli']},
)
