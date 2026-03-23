from setuptools import setup
setup(
    name='cli-anything-smtp',
    version='1.0.0',
    packages=['cli_anything.smtp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smtp=cli_anything.smtp:cli']},
)
