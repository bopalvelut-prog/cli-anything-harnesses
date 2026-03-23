from setuptools import setup
setup(
    name='cli-anything-shore',
    version='1.0.0',
    packages=['cli_anything.shore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shore=cli_anything.shore:cli']},
)
