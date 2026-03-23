from setuptools import setup
setup(
    name='cli-anything-byte',
    version='1.0.0',
    packages=['cli_anything.byte'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-byte=cli_anything.byte:cli']},
)
