from setuptools import setup
setup(
    name='cli-anything-length',
    version='1.0.0',
    packages=['cli_anything.length'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-length=cli_anything.length:cli']},
)
