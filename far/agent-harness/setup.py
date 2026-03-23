from setuptools import setup
setup(
    name='cli-anything-far',
    version='1.0.0',
    packages=['cli_anything.far'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-far=cli_anything.far:cli']},
)
