from setuptools import setup
setup(
    name='cli-anything-powerful',
    version='1.0.0',
    packages=['cli_anything.powerful'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-powerful=cli_anything.powerful:cli']},
)
