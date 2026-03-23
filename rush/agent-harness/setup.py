from setuptools import setup
setup(
    name='cli-anything-rush',
    version='1.0.0',
    packages=['cli_anything.rush'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rush=cli_anything.rush:cli']},
)
