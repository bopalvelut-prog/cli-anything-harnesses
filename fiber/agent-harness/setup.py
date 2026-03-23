from setuptools import setup
setup(
    name='cli-anything-fiber',
    version='1.0.0',
    packages=['cli_anything.fiber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fiber=cli_anything.fiber:cli']},
)
