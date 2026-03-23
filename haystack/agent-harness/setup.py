from setuptools import setup
setup(
    name='cli-anything-haystack',
    version='1.0.0',
    packages=['cli_anything.haystack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-haystack=cli_anything.haystack:cli']},
)
