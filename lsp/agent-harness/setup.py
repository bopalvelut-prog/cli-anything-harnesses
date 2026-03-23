from setuptools import setup
setup(
    name='cli-anything-lsp',
    version='1.0.0',
    packages=['cli_anything.lsp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lsp=cli_anything.lsp:cli']},
)
