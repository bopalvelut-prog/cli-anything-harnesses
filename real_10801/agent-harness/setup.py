from setuptools import setup
setup(
    name='cli-anything-real_10801',
    version='1.0.0',
    packages=['cli_anything.real_10801'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10801=cli_anything.real_10801:cli']},
)
