from setuptools import setup
setup(
    name='cli-anything-youth',
    version='1.0.0',
    packages=['cli_anything.youth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-youth=cli_anything.youth:cli']},
)
