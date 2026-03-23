from setuptools import setup
setup(
    name='cli-anything-amundsen',
    version='1.0.0',
    packages=['cli_anything.amundsen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amundsen=cli_anything.amundsen:cli']},
)
