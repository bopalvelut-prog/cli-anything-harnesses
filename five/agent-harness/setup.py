from setuptools import setup
setup(
    name='cli-anything-five',
    version='1.0.0',
    packages=['cli_anything.five'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-five=cli_anything.five:cli']},
)
