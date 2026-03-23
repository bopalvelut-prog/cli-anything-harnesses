from setuptools import setup
setup(
    name='cli-anything-fluent_bit',
    version='1.0.0',
    packages=['cli_anything.fluent_bit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fluent_bit=cli_anything.fluent_bit:cli']},
)
