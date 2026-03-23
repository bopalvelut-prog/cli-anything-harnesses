from setuptools import setup
setup(
    name='cli-anything-delombok',
    version='1.0.0',
    packages=['cli_anything.delombok'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-delombok=cli_anything.delombok:cli']},
)
