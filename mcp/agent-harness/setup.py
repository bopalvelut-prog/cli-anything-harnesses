from setuptools import setup
setup(
    name='cli-anything-mcp',
    version='1.0.0',
    packages=['cli_anything.mcp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mcp=cli_anything.mcp:cli']},
)
