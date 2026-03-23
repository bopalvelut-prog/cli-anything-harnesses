import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('comfort running')
@cli.command()
def start(): click.echo('comfort started')
if __name__ == '__main__': cli()
