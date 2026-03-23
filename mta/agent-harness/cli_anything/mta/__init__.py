import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mta running')
@cli.command()
def start(): click.echo('mta started')
if __name__ == '__main__': cli()
