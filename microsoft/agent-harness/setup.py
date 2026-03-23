from setuptools import setup
setup(
    name='cli-anything-microsoft',
    version='1.0.0',
    packages=['cli_anything.microsoft'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-microsoft=cli_anything.microsoft:cli']},
)
