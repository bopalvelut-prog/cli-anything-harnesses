from setuptools import setup
setup(
    name='cli-anything-bloom',
    version='1.0.0',
    packages=['cli_anything.bloom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bloom=cli_anything.bloom:cli']},
)
