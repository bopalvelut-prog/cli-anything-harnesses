from setuptools import setup
setup(
    name='cli-anything-suppose',
    version='1.0.0',
    packages=['cli_anything.suppose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suppose=cli_anything.suppose:cli']},
)
