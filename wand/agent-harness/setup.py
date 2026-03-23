from setuptools import setup
setup(
    name='cli-anything-wand',
    version='1.0.0',
    packages=['cli_anything.wand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wand=cli_anything.wand:cli']},
)
