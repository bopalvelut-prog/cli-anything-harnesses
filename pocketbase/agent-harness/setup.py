from setuptools import setup
setup(
    name='cli-anything-pocketbase',
    version='1.0.0',
    packages=['cli_anything.pocketbase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pocketbase=cli_anything.pocketbase:cli']},
)
