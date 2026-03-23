from setuptools import setup
setup(
    name='cli-anything-artik',
    version='1.0.0',
    packages=['cli_anything.artik'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-artik=cli_anything.artik:cli']},
)
