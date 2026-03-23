from setuptools import setup
setup(
    name='cli-anything-wonder',
    version='1.0.0',
    packages=['cli_anything.wonder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wonder=cli_anything.wonder:cli']},
)
