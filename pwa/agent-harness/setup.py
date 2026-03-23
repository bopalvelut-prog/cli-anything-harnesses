from setuptools import setup
setup(
    name='cli-anything-pwa',
    version='1.0.0',
    packages=['cli_anything.pwa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pwa=cli_anything.pwa:cli']},
)
