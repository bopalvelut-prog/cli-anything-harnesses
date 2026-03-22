from setuptools import setup
setup(
    name='cli-anything-md5sum',
    version='1.0.0',
    packages=['cli_anything.md5sum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-md5sum=cli_anything.md5sum:cli']},
)
