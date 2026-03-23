from setuptools import setup
setup(
    name='cli-anything-explain',
    version='1.0.0',
    packages=['cli_anything.explain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-explain=cli_anything.explain:cli']},
)
