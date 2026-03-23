from setuptools import setup
setup(
    name='cli-anything-restore',
    version='1.0.0',
    packages=['cli_anything.restore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restore=cli_anything.restore:cli']},
)
