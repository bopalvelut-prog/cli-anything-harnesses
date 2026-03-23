from setuptools import setup
setup(
    name='cli-anything-solaris',
    version='1.0.0',
    packages=['cli_anything.solaris'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solaris=cli_anything.solaris:cli']},
)
