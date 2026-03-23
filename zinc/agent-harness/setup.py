from setuptools import setup
setup(
    name='cli-anything-zinc',
    version='1.0.0',
    packages=['cli_anything.zinc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zinc=cli_anything.zinc:cli']},
)
