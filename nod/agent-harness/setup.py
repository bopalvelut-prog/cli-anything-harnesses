from setuptools import setup
setup(
    name='cli-anything-nod',
    version='1.0.0',
    packages=['cli_anything.nod'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nod=cli_anything.nod:cli']},
)
