from setuptools import setup
setup(
    name='cli-anything-shuffle',
    version='1.0.0',
    packages=['cli_anything.shuffle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shuffle=cli_anything.shuffle:cli']},
)
