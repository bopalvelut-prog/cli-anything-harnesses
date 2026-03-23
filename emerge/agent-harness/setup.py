from setuptools import setup
setup(
    name='cli-anything-emerge',
    version='1.0.0',
    packages=['cli_anything.emerge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emerge=cli_anything.emerge:cli']},
)
