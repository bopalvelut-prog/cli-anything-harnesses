import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('horizon running')
@cli.command()
def start(): click.echo('horizon started')
if __name__ == '__main__': cli()
