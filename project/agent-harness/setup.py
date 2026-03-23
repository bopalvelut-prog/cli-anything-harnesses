from setuptools import setup
setup(
    name='cli-anything-project',
    version='1.0.0',
    packages=['cli_anything.project'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-project=cli_anything.project:cli']},
)
