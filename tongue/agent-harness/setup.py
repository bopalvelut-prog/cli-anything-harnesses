from setuptools import setup
setup(
    name='cli-anything-tongue',
    version='1.0.0',
    packages=['cli_anything.tongue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tongue=cli_anything.tongue:cli']},
)
