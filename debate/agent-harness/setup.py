from setuptools import setup
setup(
    name='cli-anything-debate',
    version='1.0.0',
    packages=['cli_anything.debate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-debate=cli_anything.debate:cli']},
)
