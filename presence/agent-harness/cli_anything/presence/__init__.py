import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('presence running')
@cli.command()
def start(): click.echo('presence started')
if __name__ == '__main__': cli()
