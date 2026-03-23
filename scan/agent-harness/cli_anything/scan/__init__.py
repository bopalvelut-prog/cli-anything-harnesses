import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scan running')
@cli.command()
def start(): click.echo('scan started')
if __name__ == '__main__': cli()
