from setuptools import setup
setup(
    name='cli-anything-leiningen',
    version='1.0.0',
    packages=['cli_anything.leiningen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leiningen=cli_anything.leiningen:cli']},
)
