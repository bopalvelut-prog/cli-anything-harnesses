from setuptools import setup
setup(
    name='cli-anything-actiontext',
    version='1.0.0',
    packages=['cli_anything.actiontext'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-actiontext=cli_anything.actiontext:cli']},
)
