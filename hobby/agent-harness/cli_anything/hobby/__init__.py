import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hobby running')
@cli.command()
def start(): click.echo('hobby started')
if __name__ == '__main__': cli()
