import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('atomikos running')
@cli.command()
def start(): click.echo('atomikos started')
if __name__ == '__main__': cli()
