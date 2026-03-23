from setuptools import setup
setup(
    name='cli-anything-cup',
    version='1.0.0',
    packages=['cli_anything.cup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cup=cli_anything.cup:cli']},
)
