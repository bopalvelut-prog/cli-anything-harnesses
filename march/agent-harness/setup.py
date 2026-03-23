from setuptools import setup
setup(
    name='cli-anything-march',
    version='1.0.0',
    packages=['cli_anything.march'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-march=cli_anything.march:cli']},
)
