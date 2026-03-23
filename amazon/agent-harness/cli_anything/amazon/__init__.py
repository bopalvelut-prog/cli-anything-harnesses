import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon running')
@cli.command()
def start(): click.echo('amazon started')
if __name__ == '__main__': cli()
