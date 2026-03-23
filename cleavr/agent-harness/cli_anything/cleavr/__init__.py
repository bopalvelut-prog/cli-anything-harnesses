import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cleavr running')
@cli.command()
def start(): click.echo('cleavr started')
if __name__ == '__main__': cli()
