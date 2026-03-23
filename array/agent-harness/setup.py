from setuptools import setup
setup(
    name='cli-anything-array',
    version='1.0.0',
    packages=['cli_anything.array'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-array=cli_anything.array:cli']},
)
