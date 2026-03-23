from setuptools import setup
setup(
    name='cli-anything-parent',
    version='1.0.0',
    packages=['cli_anything.parent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parent=cli_anything.parent:cli']},
)
