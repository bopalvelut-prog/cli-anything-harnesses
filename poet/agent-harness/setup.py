from setuptools import setup
setup(
    name='cli-anything-poet',
    version='1.0.0',
    packages=['cli_anything.poet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poet=cli_anything.poet:cli']},
)
