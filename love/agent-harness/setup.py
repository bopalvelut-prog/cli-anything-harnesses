from setuptools import setup
setup(
    name='cli-anything-love',
    version='1.0.0',
    packages=['cli_anything.love'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-love=cli_anything.love:cli']},
)
