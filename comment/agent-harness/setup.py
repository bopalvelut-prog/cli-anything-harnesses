from setuptools import setup
setup(
    name='cli-anything-comment',
    version='1.0.0',
    packages=['cli_anything.comment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-comment=cli_anything.comment:cli']},
)
