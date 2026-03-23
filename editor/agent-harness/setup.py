from setuptools import setup
setup(
    name='cli-anything-editor',
    version='1.0.0',
    packages=['cli_anything.editor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-editor=cli_anything.editor:cli']},
)
