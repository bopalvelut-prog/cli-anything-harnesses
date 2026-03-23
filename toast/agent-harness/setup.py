from setuptools import setup
setup(
    name='cli-anything-toast',
    version='1.0.0',
    packages=['cli_anything.toast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toast=cli_anything.toast:cli']},
)
