from setuptools import setup
setup(
    name='cli-anything-transform',
    version='1.0.0',
    packages=['cli_anything.transform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transform=cli_anything.transform:cli']},
)
