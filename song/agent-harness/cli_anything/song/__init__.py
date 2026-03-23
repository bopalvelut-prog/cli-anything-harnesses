import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('song running')
@cli.command()
def start(): click.echo('song started')
if __name__ == '__main__': cli()
