from setuptools import setup
setup(
    name='cli-anything-hydrogen',
    version='1.0.0',
    packages=['cli_anything.hydrogen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hydrogen=cli_anything.hydrogen:cli']},
)
