from setuptools import setup
setup(
    name='cli-anything-alcorn',
    version='1.0.0',
    packages=['cli_anything.alcorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alcorn=cli_anything.alcorn:cli']},
)
