import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('youngster running')
@cli.command()
def start(): click.echo('youngster started')
if __name__ == '__main__': cli()
