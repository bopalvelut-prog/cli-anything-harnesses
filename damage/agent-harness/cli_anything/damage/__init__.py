import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('damage running')
@cli.command()
def start(): click.echo('damage started')
if __name__ == '__main__': cli()
