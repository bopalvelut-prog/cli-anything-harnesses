from setuptools import setup
setup(
    name='cli-anything-procedure',
    version='1.0.0',
    packages=['cli_anything.procedure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-procedure=cli_anything.procedure:cli']},
)
