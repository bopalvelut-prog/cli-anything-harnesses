from setuptools import setup
setup(
    name='cli-anything-vim',
    version='1.0.0',
    packages=['cli_anything.vim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vim=cli_anything.vim:cli']},
)
