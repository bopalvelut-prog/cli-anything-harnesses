import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('roof running')
@cli.command()
def start(): click.echo('roof started')
if __name__ == '__main__': cli()
