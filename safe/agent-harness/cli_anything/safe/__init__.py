import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('safe running')
@cli.command()
def start(): click.echo('safe started')
if __name__ == '__main__': cli()
