import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('help running')
@cli.command()
def start(): click.echo('help started')
if __name__ == '__main__': cli()
