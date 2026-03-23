from setuptools import setup
setup(
    name='cli-anything-belong',
    version='1.0.0',
    packages=['cli_anything.belong'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-belong=cli_anything.belong:cli']},
)
