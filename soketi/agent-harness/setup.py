from setuptools import setup
setup(
    name='cli-anything-soketi',
    version='1.0.0',
    packages=['cli_anything.soketi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soketi=cli_anything.soketi:cli']},
)
