import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('multimedia running')
@cli.command()
def start(): click.echo('multimedia started')
if __name__ == '__main__': cli()
