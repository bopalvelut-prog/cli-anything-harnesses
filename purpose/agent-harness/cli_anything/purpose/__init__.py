import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('purpose running')
@cli.command()
def start(): click.echo('purpose started')
if __name__ == '__main__': cli()
