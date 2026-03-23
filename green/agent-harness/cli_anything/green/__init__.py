import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('green running')
@cli.command()
def start(): click.echo('green started')
if __name__ == '__main__': cli()
