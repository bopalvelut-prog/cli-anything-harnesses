from setuptools import setup
setup(
    name='cli-anything-cppcheck',
    version='1.0.0',
    packages=['cli_anything.cppcheck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cppcheck=cli_anything.cppcheck:cli']},
)
