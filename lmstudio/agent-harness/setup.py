from setuptools import setup
setup(
    name='cli-anything-lmstudio',
    version='1.0.0',
    packages=['cli_anything.lmstudio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lmstudio=cli_anything.lmstudio:cli']},
)
