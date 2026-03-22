from setuptools import setup
setup(
    name='cli-anything-appflowy',
    version='1.0.0',
    packages=['cli_anything.appflowy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appflowy=cli_anything.appflowy:cli']},
)
