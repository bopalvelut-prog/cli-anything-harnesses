from setuptools import setup
setup(
    name='cli-anything-dress',
    version='1.0.0',
    packages=['cli_anything.dress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dress=cli_anything.dress:cli']},
)
