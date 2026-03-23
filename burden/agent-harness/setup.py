from setuptools import setup
setup(
    name='cli-anything-burden',
    version='1.0.0',
    packages=['cli_anything.burden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-burden=cli_anything.burden:cli']},
)
