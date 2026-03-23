from setuptools import setup
setup(
    name='cli-anything-bowl',
    version='1.0.0',
    packages=['cli_anything.bowl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bowl=cli_anything.bowl:cli']},
)
