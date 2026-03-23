from setuptools import setup
setup(
    name='cli-anything-wrong',
    version='1.0.0',
    packages=['cli_anything.wrong'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wrong=cli_anything.wrong:cli']},
)
