import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('group running')
@cli.command()
def start(): click.echo('group started')
if __name__ == '__main__': cli()
