import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('switch running')
@cli.command()
def start(): click.echo('switch started')
if __name__ == '__main__': cli()
