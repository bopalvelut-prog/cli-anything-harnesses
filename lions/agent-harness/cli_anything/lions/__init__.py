import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lions running')
@cli.command()
def start(): click.echo('lions started')
if __name__ == '__main__': cli()
