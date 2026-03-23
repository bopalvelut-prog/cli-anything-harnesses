from setuptools import setup
setup(
    name='cli-anything-silence',
    version='1.0.0',
    packages=['cli_anything.silence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-silence=cli_anything.silence:cli']},
)
