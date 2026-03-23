import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('useful running')
@cli.command()
def start(): click.echo('useful started')
if __name__ == '__main__': cli()
