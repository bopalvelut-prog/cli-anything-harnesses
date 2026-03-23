import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crew running')
@cli.command()
def start(): click.echo('crew started')
if __name__ == '__main__': cli()
