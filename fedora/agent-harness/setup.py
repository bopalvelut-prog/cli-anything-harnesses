from setuptools import setup
setup(
    name='cli-anything-fedora',
    version='1.0.0',
    packages=['cli_anything.fedora'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fedora=cli_anything.fedora:cli']},
)
