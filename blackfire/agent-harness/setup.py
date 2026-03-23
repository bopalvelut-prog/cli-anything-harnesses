from setuptools import setup
setup(
    name='cli-anything-blackfire',
    version='1.0.0',
    packages=['cli_anything.blackfire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blackfire=cli_anything.blackfire:cli']},
)
