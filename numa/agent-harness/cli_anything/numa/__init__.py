import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('numa running')
@cli.command()
def start(): click.echo('numa started')
if __name__ == '__main__': cli()
