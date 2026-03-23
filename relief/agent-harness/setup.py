from setuptools import setup
setup(
    name='cli-anything-relief',
    version='1.0.0',
    packages=['cli_anything.relief'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relief=cli_anything.relief:cli']},
)
