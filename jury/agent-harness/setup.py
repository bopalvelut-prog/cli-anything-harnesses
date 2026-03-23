from setuptools import setup
setup(
    name='cli-anything-jury',
    version='1.0.0',
    packages=['cli_anything.jury'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jury=cli_anything.jury:cli']},
)
