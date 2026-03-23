from setuptools import setup
setup(
    name='cli-anything-remove',
    version='1.0.0',
    packages=['cli_anything.remove'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remove=cli_anything.remove:cli']},
)
