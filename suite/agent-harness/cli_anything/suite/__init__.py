import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suite running')
@cli.command()
def start(): click.echo('suite started')
if __name__ == '__main__': cli()
