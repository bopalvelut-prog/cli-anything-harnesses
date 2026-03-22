from setuptools import setup
setup(
    name='cli-anything-hexdump',
    version='1.0.0',
    packages=['cli_anything.hexdump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hexdump=cli_anything.hexdump:cli']},
)
