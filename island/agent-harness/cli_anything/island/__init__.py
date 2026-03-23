import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('island running')
@cli.command()
def start(): click.echo('island started')
if __name__ == '__main__': cli()
