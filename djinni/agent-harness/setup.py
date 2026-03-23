from setuptools import setup
setup(
    name='cli-anything-djinni',
    version='1.0.0',
    packages=['cli_anything.djinni'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-djinni=cli_anything.djinni:cli']},
)
