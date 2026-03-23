import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mental running')
@cli.command()
def start(): click.echo('mental started')
if __name__ == '__main__': cli()
