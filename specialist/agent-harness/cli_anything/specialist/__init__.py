import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('specialist running')
@cli.command()
def start(): click.echo('specialist started')
if __name__ == '__main__': cli()
