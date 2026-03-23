from setuptools import setup
setup(
    name='cli-anything-spawn',
    version='1.0.0',
    packages=['cli_anything.spawn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spawn=cli_anything.spawn:cli']},
)
