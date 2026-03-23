from setuptools import setup
setup(
    name='cli-anything-other',
    version='1.0.0',
    packages=['cli_anything.other'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-other=cli_anything.other:cli']},
)
