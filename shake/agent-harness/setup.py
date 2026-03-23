from setuptools import setup
setup(
    name='cli-anything-shake',
    version='1.0.0',
    packages=['cli_anything.shake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shake=cli_anything.shake:cli']},
)
