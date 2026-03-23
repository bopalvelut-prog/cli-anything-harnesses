from setuptools import setup
setup(
    name='cli-anything-mov',
    version='1.0.0',
    packages=['cli_anything.mov'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mov=cli_anything.mov:cli']},
)
