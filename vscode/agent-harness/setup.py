from setuptools import setup
setup(
    name='cli-anything-vscode',
    version='1.0.0',
    packages=['cli_anything.vscode'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-vscode=cli_anything.vscode:cli',
        ],
    },
)
