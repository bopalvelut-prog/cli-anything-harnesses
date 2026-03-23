from setuptools import setup
setup(
    name='cli-anything-guitar',
    version='1.0.0',
    packages=['cli_anything.guitar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guitar=cli_anything.guitar:cli']},
)
