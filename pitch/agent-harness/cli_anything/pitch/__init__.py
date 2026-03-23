import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pitch running')
@cli.command()
def start(): click.echo('pitch started')
if __name__ == '__main__': cli()
