import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['npm', 'run', 'storybook'])
@cli.command()
def build(): subprocess.run(['npm', 'run', 'build-storybook'])
@cli.command()
def test(): subprocess.run(['npx', 'test-storybook'])
if __name__ == '__main__': cli()
