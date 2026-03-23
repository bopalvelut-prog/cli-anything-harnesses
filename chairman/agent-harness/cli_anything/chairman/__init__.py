import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chairman running')
@cli.command()
def start(): click.echo('chairman started')
if __name__ == '__main__': cli()
