import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reg running')
@cli.command()
def start(): click.echo('reg started')
if __name__ == '__main__': cli()
