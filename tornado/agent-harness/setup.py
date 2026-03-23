from setuptools import setup
setup(
    name='cli-anything-tornado',
    version='1.0.0',
    packages=['cli_anything.tornado'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tornado=cli_anything.tornado:cli']},
)
