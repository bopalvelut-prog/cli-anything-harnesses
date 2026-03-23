import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xray running')
@cli.command()
def start(): click.echo('xray started')
if __name__ == '__main__': cli()
