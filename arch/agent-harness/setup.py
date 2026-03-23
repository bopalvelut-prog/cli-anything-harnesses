from setuptools import setup
setup(
    name='cli-anything-arch',
    version='1.0.0',
    packages=['cli_anything.arch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arch=cli_anything.arch:cli']},
)
