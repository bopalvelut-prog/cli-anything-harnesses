from setuptools import setup
setup(
    name='cli-anything-beat',
    version='1.0.0',
    packages=['cli_anything.beat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beat=cli_anything.beat:cli']},
)
