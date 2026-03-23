from setuptools import setup
setup(
    name='cli-anything-windsurf',
    version='1.0.0',
    packages=['cli_anything.windsurf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-windsurf=cli_anything.windsurf:cli']},
)
