import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Make scenarios')
@cli.command()
def run(): click.echo('Make run')
if __name__ == '__main__': cli()
