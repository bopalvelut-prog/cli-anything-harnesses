import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('audience running')
@cli.command()
def start(): click.echo('audience started')
if __name__ == '__main__': cli()
