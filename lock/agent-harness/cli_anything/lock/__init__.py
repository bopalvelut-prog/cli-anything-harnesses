import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lock running')
@cli.command()
def start(): click.echo('lock started')
if __name__ == '__main__': cli()
