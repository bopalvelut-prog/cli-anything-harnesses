from setuptools import setup
setup(
    name='cli-anything-retroarch',
    version='1.0.0',
    packages=['cli_anything.retroarch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retroarch=cli_anything.retroarch:cli']},
)
