import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('want running')
@cli.command()
def start(): click.echo('want started')
if __name__ == '__main__': cli()
