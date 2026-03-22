import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def client(): subprocess.run(['chef-client'])
@cli.command()
@click.argument('cookbook')
def generate(cookbook): subprocess.run(['chef', 'generate', 'cookbook', cookbook])
if __name__ == '__main__': cli()
