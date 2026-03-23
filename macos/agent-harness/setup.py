from setuptools import setup
setup(
    name='cli-anything-macos',
    version='1.0.0',
    packages=['cli_anything.macos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-macos=cli_anything.macos:cli']},
)
