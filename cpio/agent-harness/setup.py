from setuptools import setup
setup(
    name='cli-anything-cpio',
    version='1.0.0',
    packages=['cli_anything.cpio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cpio=cli_anything.cpio:cli']},
)
