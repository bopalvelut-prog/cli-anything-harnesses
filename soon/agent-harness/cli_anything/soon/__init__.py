import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soon running')
@cli.command()
def start(): click.echo('soon started')
if __name__ == '__main__': cli()
