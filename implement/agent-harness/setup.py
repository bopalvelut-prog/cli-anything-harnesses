from setuptools import setup
setup(
    name='cli-anything-implement',
    version='1.0.0',
    packages=['cli_anything.implement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-implement=cli_anything.implement:cli']},
)
