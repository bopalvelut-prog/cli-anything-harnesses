from setuptools import setup
setup(
    name='cli-anything-mark',
    version='1.0.0',
    packages=['cli_anything.mark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mark=cli_anything.mark:cli']},
)
