from setuptools import setup
setup(
    name='cli-anything-recently',
    version='1.0.0',
    packages=['cli_anything.recently'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recently=cli_anything.recently:cli']},
)
