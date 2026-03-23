from setuptools import setup
setup(
    name='cli-anything-obligation',
    version='1.0.0',
    packages=['cli_anything.obligation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-obligation=cli_anything.obligation:cli']},
)
