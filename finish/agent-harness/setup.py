from setuptools import setup
setup(
    name='cli-anything-finish',
    version='1.0.0',
    packages=['cli_anything.finish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-finish=cli_anything.finish:cli']},
)
