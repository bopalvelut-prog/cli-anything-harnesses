from setuptools import setup
setup(
    name='cli-anything-gym',
    version='1.0.0',
    packages=['cli_anything.gym'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gym=cli_anything.gym:cli']},
)
