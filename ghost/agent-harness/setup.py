from setuptools import setup
setup(
    name='cli-anything-ghost',
    version='1.0.0',
    packages=['cli_anything.ghost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ghost=cli_anything.ghost:cli']},
)
