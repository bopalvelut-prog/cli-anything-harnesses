from setuptools import setup
setup(
    name='cli-anything-braco49',
    version='1.0.0',
    packages=['cli_anything.braco49'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco49=cli_anything.braco49:cli']},
)
