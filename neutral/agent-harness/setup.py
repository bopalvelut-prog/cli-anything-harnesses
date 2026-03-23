from setuptools import setup
setup(
    name='cli-anything-neutral',
    version='1.0.0',
    packages=['cli_anything.neutral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neutral=cli_anything.neutral:cli']},
)
