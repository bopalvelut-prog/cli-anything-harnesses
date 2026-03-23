from setuptools import setup
setup(
    name='cli-anything-verne',
    version='1.0.0',
    packages=['cli_anything.verne'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-verne=cli_anything.verne:cli']},
)
