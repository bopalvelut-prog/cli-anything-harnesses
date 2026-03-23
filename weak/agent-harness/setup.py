from setuptools import setup
setup(
    name='cli-anything-weak',
    version='1.0.0',
    packages=['cli_anything.weak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weak=cli_anything.weak:cli']},
)
