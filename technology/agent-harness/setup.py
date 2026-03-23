from setuptools import setup
setup(
    name='cli-anything-technology',
    version='1.0.0',
    packages=['cli_anything.technology'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-technology=cli_anything.technology:cli']},
)
