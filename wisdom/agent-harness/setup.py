from setuptools import setup
setup(
    name='cli-anything-wisdom',
    version='1.0.0',
    packages=['cli_anything.wisdom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wisdom=cli_anything.wisdom:cli']},
)
