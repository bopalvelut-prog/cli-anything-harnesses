from setuptools import setup
setup(
    name='cli-anything-emacs',
    version='1.0.0',
    packages=['cli_anything.emacs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emacs=cli_anything.emacs:cli']},
)
