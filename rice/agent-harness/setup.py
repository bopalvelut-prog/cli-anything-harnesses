from setuptools import setup
setup(
    name='cli-anything-rice',
    version='1.0.0',
    packages=['cli_anything.rice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rice=cli_anything.rice:cli']},
)
