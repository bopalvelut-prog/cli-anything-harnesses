from setuptools import setup
setup(
    name='cli-anything-execute',
    version='1.0.0',
    packages=['cli_anything.execute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-execute=cli_anything.execute:cli']},
)
