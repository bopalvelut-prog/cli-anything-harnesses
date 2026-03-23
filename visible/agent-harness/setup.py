from setuptools import setup
setup(
    name='cli-anything-visible',
    version='1.0.0',
    packages=['cli_anything.visible'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visible=cli_anything.visible:cli']},
)
