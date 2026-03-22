from setuptools import setup
setup(
    name='cli-anything-gitea',
    version='1.0.0',
    packages=['cli_anything.gitea'],
    install_requires=['click', 'requests'],
    entry_points={
        'console_scripts': [
            'cli-anything-gitea=cli_anything.gitea:cli',
        ],
    },
)
