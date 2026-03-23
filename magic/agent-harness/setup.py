from setuptools import setup
setup(
    name='cli-anything-magic',
    version='1.0.0',
    packages=['cli_anything.magic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-magic=cli_anything.magic:cli']},
)
