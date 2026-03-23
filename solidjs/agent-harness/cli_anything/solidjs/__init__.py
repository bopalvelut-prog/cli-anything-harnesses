import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('solidjs running')
@cli.command()
def start(): click.echo('solidjs started')
if __name__ == '__main__': cli()
