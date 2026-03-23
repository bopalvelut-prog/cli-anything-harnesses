from setuptools import setup
setup(
    name='cli-anything-step',
    version='1.0.0',
    packages=['cli_anything.step'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-step=cli_anything.step:cli']},
)
