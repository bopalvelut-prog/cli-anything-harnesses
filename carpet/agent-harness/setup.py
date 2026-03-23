from setuptools import setup
setup(
    name='cli-anything-carpet',
    version='1.0.0',
    packages=['cli_anything.carpet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-carpet=cli_anything.carpet:cli']},
)
