import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('improve running')
@cli.command()
def start(): click.echo('improve started')
if __name__ == '__main__': cli()
