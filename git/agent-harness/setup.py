from setuptools import setup
setup(
    name='cli-anything-git',
    version='1.0.0',
    packages=['cli_anything.git'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-git=cli_anything.git:cli']},
)
