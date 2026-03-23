from setuptools import setup
setup(
    name='cli-anything-unlink',
    version='1.0.0',
    packages=['cli_anything.unlink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unlink=cli_anything.unlink:cli']},
)
