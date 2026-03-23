from setuptools import setup
setup(
    name='cli-anything-tmpwatch',
    version='1.0.0',
    packages=['cli_anything.tmpwatch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tmpwatch=cli_anything.tmpwatch:cli']},
)
