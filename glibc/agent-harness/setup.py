from setuptools import setup
setup(
    name='cli-anything-glibc',
    version='1.0.0',
    packages=['cli_anything.glibc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glibc=cli_anything.glibc:cli']},
)
