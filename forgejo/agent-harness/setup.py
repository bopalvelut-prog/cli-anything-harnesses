from setuptools import setup
setup(
    name='cli-anything-forgejo',
    version='1.0.0',
    packages=['cli_anything.forgejo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-forgejo=cli_anything.forgejo:cli']},
)
