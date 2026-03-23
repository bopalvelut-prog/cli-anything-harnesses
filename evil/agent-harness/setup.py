from setuptools import setup
setup(
    name='cli-anything-evil',
    version='1.0.0',
    packages=['cli_anything.evil'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-evil=cli_anything.evil:cli']},
)
