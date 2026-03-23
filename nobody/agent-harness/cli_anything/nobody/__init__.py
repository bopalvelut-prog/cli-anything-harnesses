import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nobody running')
@cli.command()
def start(): click.echo('nobody started')
if __name__ == '__main__': cli()
