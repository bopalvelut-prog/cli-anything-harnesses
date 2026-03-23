import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('come running')
@cli.command()
def start(): click.echo('come started')
if __name__ == '__main__': cli()
