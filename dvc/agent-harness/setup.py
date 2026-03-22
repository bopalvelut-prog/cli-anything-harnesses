from setuptools import setup
setup(
    name='cli-anything-dvc',
    version='1.0.0',
    packages=['cli_anything.dvc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dvc=cli_anything.dvc:cli']},
)
