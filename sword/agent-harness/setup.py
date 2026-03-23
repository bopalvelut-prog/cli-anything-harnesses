from setuptools import setup
setup(
    name='cli-anything-sword',
    version='1.0.0',
    packages=['cli_anything.sword'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sword=cli_anything.sword:cli']},
)
