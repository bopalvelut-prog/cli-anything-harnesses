import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('earn running')
@cli.command()
def start(): click.echo('earn started')
if __name__ == '__main__': cli()
