import click
@click.group()
def cli(): pass
@cli.command()
def instances(): click.echo('Compute instances')
@cli.command()
def create(): click.echo('Compute create')
if __name__ == '__main__': cli()
