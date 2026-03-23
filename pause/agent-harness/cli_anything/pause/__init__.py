import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pause running')
@cli.command()
def start(): click.echo('pause started')
if __name__ == '__main__': cli()
