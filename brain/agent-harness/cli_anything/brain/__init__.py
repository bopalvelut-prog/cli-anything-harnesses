import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brain running')
@cli.command()
def start(): click.echo('brain started')
if __name__ == '__main__': cli()
