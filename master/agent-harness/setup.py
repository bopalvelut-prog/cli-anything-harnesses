from setuptools import setup
setup(
    name='cli-anything-master',
    version='1.0.0',
    packages=['cli_anything.master'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-master=cli_anything.master:cli']},
)
