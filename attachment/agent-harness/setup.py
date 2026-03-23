from setuptools import setup
setup(
    name='cli-anything-attachment',
    version='1.0.0',
    packages=['cli_anything.attachment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-attachment=cli_anything.attachment:cli']},
)
