from setuptools import setup
setup(
    name='cli-anything-pulse',
    version='1.0.0',
    packages=['cli_anything.pulse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pulse=cli_anything.pulse:cli']},
)
