from setuptools import setup
setup(
    name='cli-anything-chairman',
    version='1.0.0',
    packages=['cli_anything.chairman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chairman=cli_anything.chairman:cli']},
)
