from setuptools import setup
setup(
    name='cli-anything-offend',
    version='1.0.0',
    packages=['cli_anything.offend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-offend=cli_anything.offend:cli']},
)
