import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scipy running')
@cli.command()
def start(): click.echo('scipy started')
if __name__ == '__main__': cli()
