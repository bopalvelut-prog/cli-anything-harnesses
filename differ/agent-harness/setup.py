from setuptools import setup
setup(
    name='cli-anything-differ',
    version='1.0.0',
    packages=['cli_anything.differ'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-differ=cli_anything.differ:cli']},
)
