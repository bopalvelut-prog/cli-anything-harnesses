from setuptools import setup
setup(
    name='cli-anything-mode',
    version='1.0.0',
    packages=['cli_anything.mode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mode=cli_anything.mode:cli']},
)
