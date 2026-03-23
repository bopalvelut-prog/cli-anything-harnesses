from setuptools import setup
setup(
    name='cli-anything-pixel',
    version='1.0.0',
    packages=['cli_anything.pixel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pixel=cli_anything.pixel:cli']},
)
