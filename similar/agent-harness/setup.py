from setuptools import setup
setup(
    name='cli-anything-similar',
    version='1.0.0',
    packages=['cli_anything.similar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-similar=cli_anything.similar:cli']},
)
