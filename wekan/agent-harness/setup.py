from setuptools import setup
setup(
    name='cli-anything-wekan',
    version='1.0.0',
    packages=['cli_anything.wekan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wekan=cli_anything.wekan:cli']},
)
