from setuptools import setup
setup(
    name='cli-anything-progress',
    version='1.0.0',
    packages=['cli_anything.progress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-progress=cli_anything.progress:cli']},
)
