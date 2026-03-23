from setuptools import setup
setup(
    name='cli-anything-depend',
    version='1.0.0',
    packages=['cli_anything.depend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-depend=cli_anything.depend:cli']},
)
