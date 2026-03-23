import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('short running')
@cli.command()
def start(): click.echo('short started')
if __name__ == '__main__': cli()
