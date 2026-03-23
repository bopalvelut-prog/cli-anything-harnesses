import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('doppler running')
@cli.command()
def start(): click.echo('doppler started')
if __name__ == '__main__': cli()
