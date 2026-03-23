from setuptools import setup
setup(
    name='cli-anything-flush',
    version='1.0.0',
    packages=['cli_anything.flush'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flush=cli_anything.flush:cli']},
)
