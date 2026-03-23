import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lift running')
@cli.command()
def start(): click.echo('lift started')
if __name__ == '__main__': cli()
