from setuptools import setup
setup(
    name='cli-anything-obvious',
    version='1.0.0',
    packages=['cli_anything.obvious'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-obvious=cli_anything.obvious:cli']},
)
