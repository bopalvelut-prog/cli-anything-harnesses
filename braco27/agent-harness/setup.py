from setuptools import setup
setup(
    name='cli-anything-braco27',
    version='1.0.0',
    packages=['cli_anything.braco27'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco27=cli_anything.braco27:cli']},
)
