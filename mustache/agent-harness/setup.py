from setuptools import setup
setup(
    name='cli-anything-mustache',
    version='1.0.0',
    packages=['cli_anything.mustache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mustache=cli_anything.mustache:cli']},
)
