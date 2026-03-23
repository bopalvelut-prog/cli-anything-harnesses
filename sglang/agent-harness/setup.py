from setuptools import setup
setup(
    name='cli-anything-sglang',
    version='1.0.0',
    packages=['cli_anything.sglang'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sglang=cli_anything.sglang:cli']},
)
