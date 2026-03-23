from setuptools import setup
setup(
    name='cli-anything-should',
    version='1.0.0',
    packages=['cli_anything.should'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-should=cli_anything.should:cli']},
)
