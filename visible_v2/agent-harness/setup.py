from setuptools import setup
setup(
    name='cli-anything-visible_v2',
    version='1.0.0',
    packages=['cli_anything.visible_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visible_v2=cli_anything.visible_v2:cli']},
)
