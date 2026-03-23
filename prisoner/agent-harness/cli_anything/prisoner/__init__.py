import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prisoner running')
@cli.command()
def start(): click.echo('prisoner started')
if __name__ == '__main__': cli()
