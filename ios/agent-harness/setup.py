from setuptools import setup
setup(
    name='cli-anything-ios',
    version='1.0.0',
    packages=['cli_anything.ios'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ios=cli_anything.ios:cli']},
)
