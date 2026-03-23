import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lose running')
@cli.command()
def start(): click.echo('lose started')
if __name__ == '__main__': cli()
