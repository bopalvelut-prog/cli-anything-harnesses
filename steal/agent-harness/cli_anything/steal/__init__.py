import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('steal running')
@cli.command()
def start(): click.echo('steal started')
if __name__ == '__main__': cli()
