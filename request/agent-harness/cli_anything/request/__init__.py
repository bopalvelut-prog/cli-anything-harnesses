import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('request running')
@cli.command()
def start(): click.echo('request started')
if __name__ == '__main__': cli()
