import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudstack running')
@cli.command()
def start(): click.echo('cloudstack started')
if __name__ == '__main__': cli()
