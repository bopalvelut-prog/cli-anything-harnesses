from setuptools import setup
setup(
    name='cli-anything-press',
    version='1.0.0',
    packages=['cli_anything.press'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-press=cli_anything.press:cli']},
)
