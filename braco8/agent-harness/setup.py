from setuptools import setup
setup(
    name='cli-anything-braco8',
    version='1.0.0',
    packages=['cli_anything.braco8'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco8=cli_anything.braco8:cli']},
)
