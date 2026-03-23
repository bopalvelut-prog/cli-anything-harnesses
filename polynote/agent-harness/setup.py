from setuptools import setup
setup(
    name='cli-anything-polynote',
    version='1.0.0',
    packages=['cli_anything.polynote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polynote=cli_anything.polynote:cli']},
)
