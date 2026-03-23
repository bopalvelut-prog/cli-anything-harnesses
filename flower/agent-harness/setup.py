from setuptools import setup
setup(
    name='cli-anything-flower',
    version='1.0.0',
    packages=['cli_anything.flower'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flower=cli_anything.flower:cli']},
)
