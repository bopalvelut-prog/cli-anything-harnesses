import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('palm running')
@cli.command()
def start(): click.echo('palm started')
if __name__ == '__main__': cli()
