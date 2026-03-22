from setuptools import setup
setup(
    name='cli-anything-element',
    version='1.0.0',
    packages=['cli_anything.element'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-element=cli_anything.element:cli']},
)
