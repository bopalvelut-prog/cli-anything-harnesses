from setuptools import setup
setup(
    name='cli-anything-drag',
    version='1.0.0',
    packages=['cli_anything.drag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drag=cli_anything.drag:cli']},
)
