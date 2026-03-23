from setuptools import setup
setup(
    name='cli-anything-pyright',
    version='1.0.0',
    packages=['cli_anything.pyright'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyright=cli_anything.pyright:cli']},
)
