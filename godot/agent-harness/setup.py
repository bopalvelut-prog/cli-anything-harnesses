from setuptools import setup
setup(
    name='cli-anything-godot',
    version='1.0.0',
    packages=['cli_anything.godot'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-godot=cli_anything.godot:cli',
        ],
    },
)
