from setuptools import setup
setup(
    name='cli-anything-azure_windowsvm',
    version='1.0.0',
    packages=['cli_anything.azure_windowsvm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_windowsvm=cli_anything.azure_windowsvm:cli']},
)
