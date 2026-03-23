import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tire running')
@cli.command()
def start(): click.echo('tire started')
if __name__ == '__main__': cli()
