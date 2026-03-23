from setuptools import setup
setup(
    name='cli-anything-leadership',
    version='1.0.0',
    packages=['cli_anything.leadership'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leadership=cli_anything.leadership:cli']},
)
