from setuptools import setup
setup(
    name='cli-anything-imply',
    version='1.0.0',
    packages=['cli_anything.imply'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-imply=cli_anything.imply:cli']},
)
