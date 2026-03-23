from setuptools import setup
setup(
    name='cli-anything-icinga',
    version='1.0.0',
    packages=['cli_anything.icinga'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-icinga=cli_anything.icinga:cli']},
)
