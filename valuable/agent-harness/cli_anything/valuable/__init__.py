import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('valuable running')
@cli.command()
def start(): click.echo('valuable started')
if __name__ == '__main__': cli()
