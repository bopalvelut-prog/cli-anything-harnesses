from setuptools import setup
setup(
    name='cli-anything-resolution',
    version='1.0.0',
    packages=['cli_anything.resolution'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resolution=cli_anything.resolution:cli']},
)
