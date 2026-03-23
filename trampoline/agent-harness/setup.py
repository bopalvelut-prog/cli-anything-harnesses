from setuptools import setup
setup(
    name='cli-anything-trampoline',
    version='1.0.0',
    packages=['cli_anything.trampoline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trampoline=cli_anything.trampoline:cli']},
)
