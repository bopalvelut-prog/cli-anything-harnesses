from setuptools import setup
setup(
    name='cli-anything-viral',
    version='1.0.0',
    packages=['cli_anything.viral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-viral=cli_anything.viral:cli']},
)
