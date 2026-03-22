from setuptools import setup
setup(
    name='cli-anything-writefreely',
    version='1.0.0',
    packages=['cli_anything.writefreely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-writefreely=cli_anything.writefreely:cli']},
)
