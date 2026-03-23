from setuptools import setup
setup(
    name='cli-anything-drive',
    version='1.0.0',
    packages=['cli_anything.drive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drive=cli_anything.drive:cli']},
)
