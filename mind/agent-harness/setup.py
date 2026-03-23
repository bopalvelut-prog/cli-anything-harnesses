from setuptools import setup
setup(
    name='cli-anything-mind',
    version='1.0.0',
    packages=['cli_anything.mind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mind=cli_anything.mind:cli']},
)
