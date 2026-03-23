from setuptools import setup
setup(
    name='cli-anything-vim_v2',
    version='1.0.0',
    packages=['cli_anything.vim_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vim_v2=cli_anything.vim_v2:cli']},
)
