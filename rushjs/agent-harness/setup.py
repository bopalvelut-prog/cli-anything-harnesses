from setuptools import setup
setup(
    name='cli-anything-rushjs',
    version='1.0.0',
    packages=['cli_anything.rushjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rushjs=cli_anything.rushjs:cli']},
)
