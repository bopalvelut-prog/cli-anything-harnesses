import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weak running')
@cli.command()
def start(): click.echo('weak started')
if __name__ == '__main__': cli()
