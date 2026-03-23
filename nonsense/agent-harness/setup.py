from setuptools import setup
setup(
    name='cli-anything-nonsense',
    version='1.0.0',
    packages=['cli_anything.nonsense'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nonsense=cli_anything.nonsense:cli']},
)
