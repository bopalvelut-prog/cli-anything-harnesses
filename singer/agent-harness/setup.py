from setuptools import setup
setup(
    name='cli-anything-singer',
    version='1.0.0',
    packages=['cli_anything.singer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-singer=cli_anything.singer:cli']},
)
