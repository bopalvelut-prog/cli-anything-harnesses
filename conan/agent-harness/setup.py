from setuptools import setup
setup(
    name='cli-anything-conan',
    version='1.0.0',
    packages=['cli_anything.conan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conan=cli_anything.conan:cli']},
)
