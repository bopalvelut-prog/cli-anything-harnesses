import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('factory running')
@cli.command()
def start(): click.echo('factory started')
if __name__ == '__main__': cli()
