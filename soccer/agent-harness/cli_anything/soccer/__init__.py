import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('soccer running')
@cli.command()
def start(): click.echo('soccer started')
if __name__ == '__main__': cli()
