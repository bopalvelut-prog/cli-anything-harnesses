from setuptools import setup
setup(
    name='cli-anything-narrow',
    version='1.0.0',
    packages=['cli_anything.narrow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-narrow=cli_anything.narrow:cli']},
)
