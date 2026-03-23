from setuptools import setup
setup(
    name='cli-anything-same',
    version='1.0.0',
    packages=['cli_anything.same'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-same=cli_anything.same:cli']},
)
