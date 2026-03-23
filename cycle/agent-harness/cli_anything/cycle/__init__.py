import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cycle running')
@cli.command()
def start(): click.echo('cycle started')
if __name__ == '__main__': cli()
