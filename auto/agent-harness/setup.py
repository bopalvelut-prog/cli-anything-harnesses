from setuptools import setup
setup(
    name='cli-anything-auto',
    version='1.0.0',
    packages=['cli_anything.auto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-auto=cli_anything.auto:cli']},
)
