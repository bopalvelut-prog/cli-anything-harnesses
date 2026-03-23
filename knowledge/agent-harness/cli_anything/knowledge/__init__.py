import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('knowledge running')
@cli.command()
def start(): click.echo('knowledge started')
if __name__ == '__main__': cli()
