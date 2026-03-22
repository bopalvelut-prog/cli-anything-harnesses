from setuptools import setup
setup(
    name='cli-anything-cpp',
    version='1.0.0',
    packages=['cli_anything.cpp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cpp=cli_anything.cpp:cli']},
)
